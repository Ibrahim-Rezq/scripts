import os
import subprocess

def convert_all_webm_to_mp3(input_dir, output_dir):
    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"Input directory '{input_dir}' does not exist")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create output directory if it doesn't exist

    # Ensure FFmpeg is installed
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        raise EnvironmentError("FFmpeg is not installed or not in the system PATH")

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".webm"):
            input_file = os.path.join(input_dir, file_name)
            output_file = os.path.join(output_dir, os.path.splitext(file_name)[0] + ".mp3")

            # FFmpeg command to convert
            command = [
                "ffmpeg", "-i", input_file,  # Input file
                "-vn",                        # No video
                "-ar", "44100",               # Audio sampling rate
                "-ac", "2",                   # Audio channels
                "-b:a", "192k",               # Audio bitrate
                output_file                   # Output file
            ]

            try:
                subprocess.run(command, check=True)
                print(f"Converted: {input_file} -> {output_file}")
            except subprocess.CalledProcessError as e:
                print(f"Error converting {input_file}: {e}")

# Example usage
if __name__ == "__main__":
    input_directory = "./hello"    # Replace with your input directory
    output_directory = "./out"  # Replace with your output directory
    convert_all_webm_to_mp3(input_directory, output_directory)
