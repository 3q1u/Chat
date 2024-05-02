import edge_tts
import playsound

voice = 'zh-CN-YunxiNeural'
rate = '+10%'
volume = '+0%'

async def speak(text):
    tts = edge_tts.Communicate(text=text, voice=voice, rate=rate, volume=volume)
    await tts.save('temp/response.wav')
    playsound.playsound('temp/response.wav')