# AVATAR CODE GENERATOR FOR NEURONIOLIVE
# by @bunnysammy_
#
# Running this code will generate a text file with the CSS code
# for whatever NeuronioLive member you select in whichever mode
# you want.

import requests, webbrowser

print('AVATAR CODE GENERATOR FOR NEURONIOLIVE')
print('')

print('Choose a member:')
print('[1] Mari')
print('[2] Ferreira')
print('[3] David')
print('[4] Lou')
member_number = str(input())

if member_number == '1':
    member_id = '290586962144788480'
elif member_number == '2':
    member_id = '405680071744028673'
elif member_number == '3':
    member_id = '225443969885143041'
elif member_number == '4':
    member_id = '429801182274387971'
else:
    member_id = 'error'

print('Choose an avatar type. Write the name without quotes.')
types = ('default', 'careca', 'halloween-2021', 'natal-2021', 'sus')
print(types)
avatar_type = str(input())

full = input('[0] Just head or [1] Full body?')
if int(full) == 1:
    print("Full")
    url_closed = f'https://raw.githubusercontent.com/bunny-sammy/NeuronioLive/main/avatars/{avatar_type}/avatar_{member_number}_closed_full.png'
    url_open = f'https://raw.githubusercontent.com/bunny-sammy/NeuronioLive/main/avatars/{avatar_type}/avatar_{member_number}_open_full.png'
else:
    print("Smol")
    url_closed = f'https://raw.githubusercontent.com/bunny-sammy/NeuronioLive/main/avatars/{avatar_type}/avatar_{member_number}_closed.png'
    url_open = f'https://raw.githubusercontent.com/bunny-sammy/NeuronioLive/main/avatars/{avatar_type}/avatar_{member_number}_open.png'

code_data = """/***Two Images w/ Animation***/
/*User*/ img:not([src*='<MEMBER_ID>']), img:not([src*='UserID']) + div  { display:none; }
/*Avatar*/ img[class*="avatar"] { content:url("<URL_CLOSED>"); }
/*Speaking*/ img[class*="avatarSpeaking"] { content:url("<URL_OPEN>"); }
/*Flex Set*/ html, body, img, div, span, ul, li { display:flex; }
/*Center Image*/ html { height:100%; justify-content:center; }
/*Hide Scrollbars*/ body { overflow:hidden; }
/*List CSS*/ ul[class*="voiceStates"] { padding-inline:0; margin-block:0; margin-top: 5px; }
/*List Item CSS*/ li[class*="voiceState"] { flex-direction:column; align-items:center; margin:0; height:unset; }
/*Avatar CSS*/ img[class*="avatar"] { width:100%; height:auto; border:0; border-radius:0; margin:0; float:unset; filter:brightness(50%); transition: all 0.2s ease-in-out; }
/*Speaking CSS*/ img[class*="avatarSpeaking"] { position:relative; animation:speak-now 0.2s; filter:brightness(95%); }
/*Username CSS*/ div[class*="user"] {position:absolute; text-align:center; padding:0; bottom:0; } span[class*="name"] { margin-bottom: 0.5em; }
/*Animation*/ @keyframes speak-now { 50%{ bottom:3px; } }"""

code_data_old = """li.voice-state:not([data-reactid*='<MEMBER_ID>']) { display:none; }
.avatar {
  content:url('<URL_CLOSED>');
  height:auto !important;
  width:auto !important;
  border-radius:0% !important;
  filter: brightness(80%); 
/*Change brightness to 100%, if you don’t want the image to dim*/
}

.speaking {
  border-color:rgba(0,0,0,0) !important;
  position:relative;
  animation-name: speak-now;
  animation-duration: 1s;
  animation-fill-mode:forwards;
  filter: brightness(100%);
content:url('<URL_OPEN>');
}

@keyframes speak-now {
  0% { bottom:0px;  }
  15% { bottom:10px;  }
  30% { bottom:0px;  }
}

li.voice-state{ position: static; }
div.user{ position: absolute; left:40%; bottom:5%; }

body { background-color: rgba(0, 0, 0, 0); margin: 0px auto; overflow: hidden; }"""

code_data = code_data.replace('<MEMBER_ID>', member_id)
code_data = code_data.replace('<URL_CLOSED>', url_closed)
code_data = code_data.replace('<URL_OPEN>', url_open)

text_file = open("code.txt", "w")
print('Opened text file.')
n = text_file.write(code_data)
print('Wrote to file.')
text_file.close()
webbrowser.open("code.txt")