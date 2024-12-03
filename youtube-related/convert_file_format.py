import os
import subprocess

def convert_file(input_file, output_dir, to_format):
    """
    Converts a single file to a specified format.

    Args:
        input_file (str): Path to the input file to convert.
        output_dir (str): Path to the output directory for the converted file.
        to_format (str): Format to convert the file to (e.g., '.mp3').
    """
    # Ensure the input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' does not exist.")

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Ensure FFmpeg is installed
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        raise EnvironmentError("FFmpeg is not installed or not in the system PATH.")

    # Construct the output file path
    file_name = os.path.basename(input_file)
    output_file = os.path.join(output_dir, os.path.splitext(file_name)[0] + to_format)

    # FFmpeg command for conversion
    command = [
        "ffmpeg", "-i", input_file,  # Input file
        "-vn",                        # No video (if applicable)
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
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    import argparse

    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Convert a single file to a specified format using FFmpeg.")
    parser.add_argument("input_file", help="Path to the input file to convert.")
    parser.add_argument("output_dir", help="Path to the output directory for the converted file.")
    parser.add_argument("to_format", help="File format to convert to (e.g., '.mp3').")

    args = parser.parse_args()

    # Call the conversion function
    try:
        convert_file(args.input_file, args.output_dir, args.to_format)
    except Exception as e:
        print(f"Error: {e}")
