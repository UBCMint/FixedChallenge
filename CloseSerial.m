% Use the following commands to close the arduino serial connection so 
% that the MintData script can be re-run without having to restart matlab 
% load('serialObj.mat')
% fclose(instrfind(arduino))
% clear all

function [] = CloseSerial()
    load('serialObj.mat','arduino');
    fclose(instrfind(arduino));
    clear all;
    disp('Serial connection to arduino closed');
end