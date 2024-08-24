# app/main.py

import os
from sample_module import reverse_string

if os.getenv('DEBUG') == 'True':
    import debugpy # type: ignore
    debugpy.listen(('0.0.0.0', 5678))
    print("Waiting for debugger attach...")
    debugpy.wait_for_client()  # Wait until the debugger is attached
    print("Debugger attached!")

# Your main code logic starts here
def main():
    print("Running the main function! :-)")
    print(reverse_string('hello world'))

if __name__ == "__main__":
    main()
