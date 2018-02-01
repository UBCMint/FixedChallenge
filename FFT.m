
function processthedata()
v = load(data)  %load the vector with voltage readings  
amount = length(d);% reading the data
t = (0:amount-1); % or t = load(time)                                        % Convert To ‘seconds’ From ‘milliseconds’
%v = d(:,2);  
%t = B;
% Voltage (?)
L = length(t);
Ts = mean(diff(t));                                     % Sampling Interval (sec)
Fs = 1/Ts;                                              % Sampling Frequency
Fn = Fs/2;
vc = v - mean(v);                                       % Subtract Mean (‘0 Hz’) Component
FTv = fft(vc)/L;                                        % Fourier Transform
Fv = linspace(0, 1, fix(L/2)+1)*Fn;                     % Frequency Vector (Hz)
Iv = 1:length(Fv);                                      % Index Vector
figure(1)
plot(Fv, abs(FTv(Iv))*2);
grid;
xlabel('Frequency (Hz)');
ylabel('Amplitude (V?)');
end
% 
% function ourfft()
% 
% Fs = 200;             % Sampling frequency                    
% T = 1/Fs;             % Sampling period       
% L = 1500;             % Length of signal (how many data points)
% t = (0:L-1)*T;        % Time vector
% 
% DataPoints = [];
% 
% figure(1)
% plot=plot(t,DataPoints);
% grid;
% 
% FT_P = fft(plot)/;
% Fv = linspace(0, 1, fix(L/2)+1)*Fn;                                 % Frequency Vector
% Iv = 1:length(Fv);
% 
% i = 0
% 
% while i>=0
% FFT = fft(vectory, vectorx) %fft 
%        
% P2 = abs(Y/L);
% P1 = P2(1:L/2+1);
% P1(2:end-1) = 2*P1(2:end-1); %single sided amp
% 
% f = Fs*(0:(L/2))/L;
% plot(f,P1) 
% title('Single-Sided Amplitude Spectrum of X(t)')
% xlabel('f (Hz)')
% ylabel('|P1(f)|')
% 
% end
% end
% 
% %takes the points in a vector
% 
% function [Y] = fDFT(x)
% %The discrete Fourier transform of input data x
% Lx = length(x);
% NDFT = 2^nextpow2(Lx); % Next power of 2 from length of x
% X =[x zeros(1,NDFT-Lx)];
% Y = zeros(1,NDFT);
% for k = 0:NDFT-1
% Y(k+1) = 0;
% for n = 0:NDFT-1
% Y(k+1)=Y(k+1)+(X(n+1)*exp((-1j)*2*pi*k*n/Lx));
% end
% end
% end