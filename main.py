from pydub import AudioSegment

# Function to generate empty audio segment
def generate_empty_audio(duration_ms):
    return AudioSegment.silent(duration=duration_ms)


if __name__ =="__main__":
    final_audio  = generate_empty_audio(10)
    with open("keylog.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            key = line.split(" ")[0]
            delay = line.split(" ")[1]
            file = AudioSegment.from_file("sound/mouse_click.mp3")
            empty_audio = generate_empty_audio(int(delay))
            concatenated_audio = empty_audio + file
            final_audio += concatenated_audio
        output_file = "final_export.mp3"
        final_audio.export(output_file, format="mp3")

