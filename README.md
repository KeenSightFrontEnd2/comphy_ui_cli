# Comphy UI CLI

This CLI script provides a command line interface to automate various tasks for the Comphy UI.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- `click` module
- `Pillow` module
- Comphy UI - Install from [here](https://github.com/comfyanonymous/ComfyUI?tab=readme-ov-file#installing)
- comfy-cli - Install from [here](https://github.com/Comfy-Org/comfy-cli)
- Model or models of your choice - Can be found on hugging face etc.

You can install the required Python modules using pip:

```sh
pip install click pillow
```

## Usage

Navigate to the directory containing comphy_cli.py and run the script with the desired command.

- Start the Comphy UI. Optionally, you can run it on CPU if the --cpu flag is provided.

```sh
python comphy_cli.py start_ui [--cpu]
```

- Stop the Comphy UI

```sh
python comphy_cli.py stop_ui
```

- Check the Status of the Comphy UI

```sh
python comphy_cli.py status_ui
```

- Load a Model

```sh
python comphy_cli.py load_model <model_path>
```

- Load a workflow from a JSON file.

```sh
python comphy_cli.py load_workflow <workflow_file>
```

- Refresh a specific component in the Comphy UI.

```sh
python comphy_cli.py refresh_component <component>
```

- Loads a full workflow from a generated image file (PNG, WebP, FLAC).

```sh
python comphy_cli.py load_from_image <image_file>
```

- Save the Current Workflow

```sh
python comphy_cli.py save_workflow <workflow_file>
```

- Set the Config File for Model Search Paths

```sh
python comphy_cli.py set_config <config_file>
```

- Run a Custom Command

```sh
python comphy_cli.py run_custom "<your_custom_command>"
```

- Resize an Image to a Specified Aspect Ratio

```sh
python comphy_cli.py resize_image <image_path> <target_aspect_ratio> <output_path>
```

- Generates an image based on a prompt and resolution using comfy-cli.

```sh
python comphy_cli.py generate_image "<prompt>" <resolution> <output_path>
```
