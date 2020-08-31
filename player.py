import sounddevice as sd
import soundfile as sf
from playsound import playsound
import os
from scipy.io.wavfile import write
import uuid
# from pydub import AudioSegment

duration = int(input("Enter the duration: "))  # recording duration
fs = 44000  # fs

sd.default.samplerate = fs  # default fs
sd.default.channels = 2  # default channel


# generating unique uuid for filename
def gen_filename():
    return './sound-files/' + str(uuid.uuid1()) + '.wav'


# converting into flac format
def convert_file_flac(fs, filename):
    try:
        data, fs = sf.read(filename)  # extract the file
        # new converted filename
        new_filename = str(input("enter the converted filename: "))
        sf.write('./sound-files/'+new_filename+'.flac',
                 data, fs)  # converting into flac format
        return new_filename
    except Exception as f:
        print("message: ", f)


# converting into .mp3
def convert_file_mp3(filename):
    try:
        sound = AudioSegment.from_wav('sample.wav')
        # new converted filename
        new_filename = str(input("enter the converted filename: "))
        sound.export(new_filename + '.mp3', format='mp3')
    except Exception as g:
        print("message: " + g)


# recording the sound
try:
    record_start = sd.rec(int(duration * fs))  # recording start
    sd.wait()  # wait until the recording is finished
    filename = gen_filename()
    write(filename, fs, record_start)  # save as WAV file
    print("Convertion")
    print("1. Convert into FLAC format")
    print("2. Convert into MP3 format")
    print("Press any enter key to exit")
    try:
        option = int(input('Enter choice'))

        if option == 1:
            new_filename = convert_file_flac(fs, filename)
        elif option == 2:
            pass
        else:
            pass
    except Exception as i:
        pass


    try:
        user_res = str(input("Do you want to play the music Y/N?"))
        if user_res.lower() == 'y':
            playsound(filename)
        elif user_res.lower() == 'n':
            exit(0)
        else:
            print("Wrong input")
            exit(0)
    except Exception as f:
        exit(0)

except Exception as e:
    print("message:", e)
