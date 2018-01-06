% Save the serial port name in comPort variable.
comPort = '/dev/tty.usbserial-AL01QIAZ';   

if(~exist('serialFlag','var'))
[arduino,serialFlag] = setupSerial(comPort);
end

% Setup graph
figure(1)  
ax = gca;
set(ax, 'YDir', 'reverse');
axis([-3 4 0.5 5])
xlabel('X End-effector Position', 'fontsize', 12)
ylabel('Y End-effector Position', 'fontsize', 12)
title('End-effector Position in Space', 'fontsize', 14)

t = 1;

while t>0
   %clear all;
   mode = 'x';
   x = readVal(arduino,mode);

   mode = 'y';
   y = readVal(arduino,mode);
    
   disp('x');
   disp(x);
   disp('y');
   disp(y);
   
   hold on;
   p = plot(str2double(x),str2double(y),'*');    
   set(p,'linewidth',2);
   drawnow limitrate;
   hold all;
   delete(p)
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
    set(obj,'BaudRate',115200);
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