import subprocess
import time

def run_command_from_file(file_path):
    while True:
        try:
            with open(file_path, 'r') as file:
                command = file.read().strip()
                subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Command '{command}' returned non-zero exit status: {e}")
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            break
        except KeyboardInterrupt:
            print("\nKeyboard Interrupt. Stopping the loop.")
            break
        time.sleep(1)  # Adjust the delay between command executions

if __name__ == "__main__":
    script_file = "~/vulture_bee_cam/scripts/record_video.sh"
    run_command_from_file(script_file)
