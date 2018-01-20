% After arduino has been setup, run MintData.m to start data acquisition
% Use CTRL+C to terminate script
% Run CloseSerial.m script to close the arduino serial connection
% Once arduino is initially setup, will continuously perform data
% acquisition

% Timestamp and channel data saved to text file 'data.txt'
% Real-time plot of channel data displayed 

function [] = MintData()

    close all;
    
    global arduino;
    % Save the serial port name in comPort variable.
    %comPort = '/dev/tty.usbserial-AL01QIAZ';   
    %comPort = '/dev/cu.usbmodem1411';
    comPort = '/dev/cu.usbmodem1421';
    if(~exist('serialFlag','var'))
    [arduino,serialFlag] = setupSerial(comPort);
    end

    % Setup file
    fileID = fopen('data.txt','wt');
    if (fileID == -1)
       disp('file not valid');
    end 
    fprintf(fileID,'%6s %12s\n','time','ch1');
    fclose(fileID);

    % Create clean up object to execute when program terminates
    fileID = fopen('data.txt','a');
    cleanupObj = onCleanup(@() cleanup(fileID));

    % Setup graph
    figure(1)  
    ax = gca;
    set(ax, 'YDir', 'reverse');
    ylim([0.5 5]);
    xlim([0 10]);
    xlabel('Time', 'fontsize', 12)
    ylabel('Channel 1 Signal', 'fontsize', 12)
    title('EEG vs Time', 'fontsize', 14)

    % Initialize loop and timestamp
    t = 1;
    t0 = datevec(now);

    while t>0
       % Get timestamp
       t1 = datevec(now);
       x = etime(t1,t0);

       % Read data from arduino
       mode = 'y'; % channel 1
       y = readVal(arduino,mode);

       % Write to file
       fprintf(fileID,'%6.2f %12.8f\n', x, str2double(y));

       %disp('x');
       %disp(x);
       %disp('y');
       %disp(y);

       hold on;
       p = plot(x,str2double(y), '-o');    
       set(p,'linewidth',2);
       xlim([x-5 x+5]);
       drawnow limitrate;
    end
end

function[obj,flag] = setupSerial(comPort)
    % It accept as the entry value, the index of the serial port
    % Arduino is connected to, and as output values it returns the serial
    % element obj and a flag value used to check if when the script is compiled
    % the serial element exists yet.
    flag = 1;
    % Initialize Serial object
    obj = serial(comPort);
    set(obj,'Timeout',600);%added
    set(obj,'DataBits',8);
    set(obj,'StopBits',1);
    set(obj,'BaudRate',9600);
    set(obj,'Parity','none');
    fopen(obj);
    a = 'b';
    while (a~='a')
    a=fread(obj,1,'uchar');
    end
    if (a=='a')
    disp('Serial read');
    end
    fprintf(obj,'%c','a');
    mbox = msgbox('Serial Communication setup'); uiwait(mbox);
    fscanf(obj,'%u');
end

function [output] = readVal(s,command)
    % Serial send read request to Arduino
    fprintf(s,command);
    
    % Read value returned via Serial communication
    output = fgetl(s);
end

function cleanup(fileID)
    global arduino;
    fclose(fileID);
    save('serialObj.mat', 'arduino');
    disp('goodbye');
    
end
    

