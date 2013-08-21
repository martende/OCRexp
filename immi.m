clear all; close all; clc;

function retval = normalize (Bts)
    aBts = abs(Bts);
    minBts = min(min(aBts));
    maxBts = max(max(aBts));
    retval = (aBts - minBts)*256 / (maxBts-minBts);
endfunction

function fftshow(filename)
    A=imread(filename); % load image
    Abw=rgb2gray(A); % make image black-and-white
    subplot(2,2,1), imshow(A);
    %subplot(2,2,2), imshow(Abw);
    % A2=double(A); % change form unit8 to double
    Abw=double(Abw);
    Bt=fft2(Abw); Bts=fftshift(Bt);
    subplot(2,2,2);
    imshow(normalize(Bts)); axis image; colorbar;

endfunction

%subplot(2,2,4), pcolor(uint8(log(abs(Bts))));
%colormap(gray), set(gca,'Xtick',[],'Ytick',[])

figure(1);
fftshow('image1.png');
figure(2);
fftshow('image2.png');
figure(3);
fftshow('image3.png');

