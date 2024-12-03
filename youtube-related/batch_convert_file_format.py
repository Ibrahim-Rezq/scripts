import os
import subprocess

def convert_files(input_dir, output_dir, from_format, to_format):
    """
    Converts all files of a given format in the input directory to another format in the output directory.

    Args:
        input_dir (str): Path to the input directory.
        output_dir (str): Path to the output directory.
        from_format (str): Format of files to convert from (e.g., '.webm').
        to_format (str): Format of files to convert to (e.g., '.mp3').
    """
    # Ensure input directory exists
    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"Input directory '{input_dir}' does not exist.")

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Ensure FFmpeg is installed
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        raise EnvironmentError("FFmpeg is not installed or not in the system PATH.")

    # Process each file in the input directory
    for file_name in os.listdir(input_dir):
        if file_name.lower().endswith(from_format.lower()):
            input_file = os.path.join(input_dir, file_name)
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
    parser = argparse.ArgumentParser(description="Convert files from one format to another using FFmpeg.")
    parser.add_argument("input_dir", help="Path to the input directory containing files to convert.")
    parser.add_argument("output_dir", help="Path to the output directory for converted files.")
    parser.add_argument("from_format", help="File format to convert from (e.g., '.webm').")
    parser.add_argument("to_format", help="File format to convert to (e.g., '.mp3').")

    args = parser.parse_args()

    # Call the conversion function
    try:
        convert_files(args.input_dir, args.output_dir, args.from_format, args.to_format)
    except Exception as e:
        print(f"Error: {e}")
