# CLIHelper: A Command-Line Interface Assistant

CLIHelper is a command-line interface (CLI) tool designed to assist users by generating CLI commands or a series of CLI commands based on user input. Utilizing OpenAI's GPT model, it provides detailed responses and ensures a comprehensive understanding of the required tasks.

## Installation

CLIHelper is now available for installation via pip. To install CLIHelper on your system, ensure you have Python and pip installed. If you do not have them installed, please visit the [official Python website](https://www.python.org/) for installation instructions.

Once Python and pip are set up, you can install CLIHelper using the following command:

```sh
pip install altcli_helper
```

This command will download and install CLIHelper along with its required dependencies, making it ready to use on your system.

If you encounter any permission issues during the installation, you might need to run the command with administrative privileges or use a virtual environment. For administrative privileges, you can use `sudo` on Linux/macOS:

```sh
sudo pip install altcli_helper
```

Or, for Windows, run the command prompt as an administrator. Alternatively, you can install CLIHelper in a virtual environment to avoid the need for administrative privileges:

```sh
python -m venv venv
source venv/bin/activate  # On Linux/macOS
.\venv\Scripts\activate  # On Windows
pip install altcli_helper
```

Once installed, you can proceed to use CLIHelper as described in the Usage section.

## Setup

Before you start using CLIHelper, you need to set up the `OPENAI_API_KEY` environment variable to store your OpenAI API key. This key is essential for CLIHelper to interact with OpenAI's GPT model.

### Setting Up OPENAI_API_KEY

1. **Obtain an API Key:** If you haven't already, create an account on [OpenAI](https://openai.com/) and follow the instructions to generate an API key.

2. **Export the API Key:** You need to add the API key to your environment variables. You can do this by adding an export command to your shell configuration file. The exact file and command depend on your operating system and shell. Below are examples for some common shells:

   - **Bash (Linux/macOS):** Add the following line to your `.bashrc` or `.bash_profile` file:

     ```sh
     export OPENAI_API_KEY='your_api_key_here'
     ```

   - **Zsh (Linux/macOS):** If you're using Zsh, add the line to your `.zshrc` file instead.

   - **Fish (Linux/macOS):** If you're using Fish shell, you can set the environment variable with the `set` command, and you may want to add it to your `config.fish` file:

     ```sh
     set -x OPENAI_API_KEY 'your_api_key_here'
     ```

   - **PowerShell (Windows):** Add the following line to your profile file, which is typically located at `$Home\[My ]Documents\PowerShell\Microsoft.PowerShell_profile.ps1`:

     ```powershell
     $env:OPENAI_API_KEY='your_api_key_here'
     ```

   - **Command Prompt (Windows):** You can set environment variables for the session using the `set` command:

     ```cmd
     set OPENAI_API_KEY=your_api_key_here
     ```

     To make this change permanent, you can use the System Properties window.

3. **Verify the Setup:** After adding the export command, restart your terminal or run the source command to apply the changes. You can verify that the environment variable is set up correctly by running:

   - On Linux/macOS:

     ```sh
     echo $OPENAI_API_KEY
     ```

   - On Windows (PowerShell):

     ```powershell
     echo $env:OPENAI_API_KEY
     ```

   You should see your API key printed to the terminal.

Now that you have set up the `OPENAI_API_KEY` environment variable, CLIHelper can access it, and you can proceed to use the tool as described in the Usage section.

## Usage

CLIHelper is straightforward to use and can be executed directly from the command line.

### Basic Command Generation

For generating a CLI command based on your request:

```sh
clih "Your request here"
```

Example:

```sh
clih "How to list all files in a directory?"
```

### Command Generation with Rationale

If you want to see the rationale behind the recommended commands, in addition to the commands themselves, use the `-s` or `--show-rationale` flag:

```sh
clih -s "Your request here"
```

or

```sh
clih --show-rationale "Your request here"
```

Example:

```sh
clih -s "How to list all files in a directory?"
```

This will print out a detailed rationale explaining why certain commands are recommended, followed by the recommended commands themselves.

## Contact

For any inquiries or issues, please contact D0rkKnight at [shouhanzen@gmail.com](mailto:shouhanzen@gmail.com).

## License

This project is open source and available under the [MIT License](LICENSE).
