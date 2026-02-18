from pyscript import document, when
from js import window


class Instrument:
    def __init__(self):
        self.sound_text = ""
        self.display_text = ""

    def make_noise(self):
        if self.sound_text:
            utterance = window.SpeechSynthesisUtterance.new(self.sound_text)
            utterance.lang = "th-TH"
            window.speechSynthesis.speak(utterance)
        return self.display_text


class Violin(Instrument):
    def __init__(self):
        self.sound_text = "วี๊ วี๊ วี้"
        self.display_text = "🎻 ไวโอลินกำลังสี!"


class Trumpet(Instrument):
    def __init__(self):
        self.sound_text = "ปู้ ปู้ ป้า"
        self.display_text = "🎺 ทรัมเป็ตกำลังเป่า!"


class Drum(Instrument):
    def __init__(self):
        self.sound_text = "ตุ้ม ตุ้ม ปั้ง"
        self.display_text = "🥁 กลองกำลังตี!"


class Flute(Instrument):
    def __init__(self):
        self.sound_text = "ฟิ้ว ฟิ้ว วิ้ว"
        self.display_text = "🪈 ขลุ่ยกำลังเป่า!"


@when("click", "#btn_sound")
def play_sound(event):
    choice = document.getElementById("instrument_selector").value
    instrument = None

    if choice == "violin":
        instrument = Violin()
    elif choice == "trumpet":
        instrument = Trumpet()
    elif choice == "drum":
        instrument = Drum()
    elif choice == "flute":
        instrument = Flute()

    if instrument:
        text = instrument.make_noise()
        document.getElementById("output").innerText = text
