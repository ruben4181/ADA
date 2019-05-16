function varargout = GUITORTUGA(varargin)
% GUITORTUGA MATLAB code for GUITORTUGA.fig
%      GUITORTUGA, by itself, creates a new GUITORTUGA or raises the existing
%      singleton*.
%
%      H = GUITORTUGA returns the handle to a new GUITORTUGA or the handle to
%      the existing singleton*.
%
%      GUITORTUGA('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in GUITORTUGA.M with the given input arguments.
%
%      GUITORTUGA('Property','Value',...) creates a new GUITORTUGA or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before GUITORTUGA_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to GUITORTUGA_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help GUITORTUGA

% Last Modified by GUIDE v2.5 15-May-2019 16:14:41

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @GUITORTUGA_OpeningFcn, ...
                   'gui_OutputFcn',  @GUITORTUGA_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before GUITORTUGA is made visible.
function GUITORTUGA_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to GUITORTUGA (see VARARGIN)

% Choose default command line output for GUITORTUGA
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes GUITORTUGA wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = GUITORTUGA_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double


% --- Executes during object creation, after setting all properties.
function edit1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit2_Callback(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit2 as text
%        str2double(get(hObject,'String')) returns contents of edit2 as a double


% --- Executes during object creation, after setting all properties.
function edit2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit3_Callback(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit3 as text
%        str2double(get(hObject,'String')) returns contents of edit3 as a double


% --- Executes during object creation, after setting all properties.
function edit3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

function [x] = solveQuadratic(a, b, c)
    x = zeros(2,1);
    d = sqrt(b^2 - 4*a*c);
    x(1) = ( -b + d ) / (2*a);
    x(2) = ( -b - d ) / (2*a);

function [vel0] = vel0Tortuga(a, b)
    vel0=(-b)/2*a;

function [acel] = acelTortuga(a)
    acel=-(2*a);

function [vel] = velTortuga(a, b, t)
    vel=(-2*a*t)+b;
% --- Executes on button press in pushbutton1.
function[pos] = posTortuga(a, b, c, t)
    pos= -(a)*(t.^2)+(b)*(t)+c;

function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

aValue=str2double(get(handles.edit1, 'String'));
bValue=str2double(get(handles.edit2, 'String'));
cValue=str2double(get(handles.edit3, 'String'));

position=posTortuga(aValue, bValue, cValue, 0);
vel=velTortuga(aValue, bValue, 0);
acel=acelTortuga(aValue);

x=solveQuadratic(aValue, bValue, 0);
x2=solveQuadratic(aValue, bValue, cValue-10);
set(handles.text7, 'String', strcat('Posicion incial: ', num2str(position)));
set(handles.text8, 'String', strcat('Velocidad inicial: ', num2str(vel)));
set(handles.text9, 'String', strcat('Aceleracion inicial: ', num2str(acel)));
set(handles.text10, 'String', strcat('Las posiciones donde vuelve al inicio son cuando t=', num2str(x(1)), ' y t=', num2str(x(2))));
set(handles.text11, 'String', strcat('En tiempo=', num2str(x2(1)), ' y tiempo=', num2str(x2(2)), ' la tortuga esta a 10 cm del punto de partida'));

vel10=velTortuga(aValue, bValue, x2(1));
vel102=velTortuga(aValue, bValue, x2(2));
disp(vel10);

set(handles.text12, 'String', strcat('Velocidades a 10cm: ', num2str(vel10), ',', num2str(vel102)  ));
set(handles.text13, 'String', strcat('la aceleracion es constante y es la misma del inicio'))


time = 0:0.5:40;
pos_time = 0:0.5:40;
vel_time= 0:0.5:40;
acel_time=0:0.5:40;
index=1
for c = time
   pos_time(index)=posTortuga(aValue, bValue, cValue, time(index));
   val_time(index)=velTortuga(aValue, bValue, time(index));
   acel_time(index)=acelTortuga(aValue);
   index=index+1;
end

figure;
plot(time, pos_time);
title('Posicion vs Tiempo');
xlabel('Tiempo 0<t<40');
ylabel('Posicion');
figure;
plot(time, vel_time);
title('Velocidad vs Tiempo');
xlabel('Tiempo 0<t<40');
ylabel('Velocidad');
figure;
plot(time, acel_time);
title('Aceleracion vs Tiempo');
xlabel('Tiempo 0<t<40');
ylabel('Aceleracion');

% --- If Enable == 'on', executes on mouse press in 5 pixel border.
% --- Otherwise, executes on mouse press in 5 pixel border or over edit1.
function edit1_ButtonDownFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)



function edit4_Callback(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit4 as text
%        str2double(get(hObject,'String')) returns contents of edit4 as a double


% --- Executes during object creation, after setting all properties.
function edit4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
