import click
import subprocess
from PIL import Image

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        click.echo(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        click.echo(f"Error: {e.stderr.decode()}", err=True)

def change_aspect_ratio(image_path, target_aspect_ratio, output_path):
    # Open the image
    image = Image.open(image_path)
    
    # Get current dimensions
    width, height = image.size
    current_aspect_ratio = width / height
    
    # Determine new dimensions
    if current_aspect_ratio < target_aspect_ratio:
        # Extend width
        new_width = int(target_aspect_ratio * height)
        new_height = height
    else:
        # Extend height
        new_width = width
        new_height = int(width / target_aspect_ratio)
    
    # Resize the image to the new dimensions
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
    
    # Create a new image with the target aspect ratio and paste the resized image onto it
    new_image = Image.new("RGB", (new_width, new_height))
    new_image.paste(resized_image)
    
    # Save the resulting image
    new_image.save(output_path)

@click.group()
def cli():
    """CLI for automating Comphy UI commands."""
    pass

@click.command()
@click.option('--gpu', default=True, is_flag=True, help="Use GPU if available, otherwise run on CPU (slow)")
def start_ui(gpu):
    """Start the Comphy UI."""
    command = "comphy-ui start"
    if not gpu:
        command += " --cpu"
    run_command(command)

@click.command()
def stop_ui():
    """Stop the Comphy UI."""
    command = "comphy-ui stop"
    run_command(command)

@click.command()
def status_ui():
    """Check the status of the Comphy UI."""
    command = "comphy-ui status"
    run_command(command)

@click.command()
@click.argument('model_path')
def load_model(model_path):
    """Load a model (ckpt, safetensors, diffusers)."""
    command = f"comphy-ui load_model {model_path}"
    run_command(command)

@click.command()
@click.argument('workflow_file')
def load_workflow(workflow_file):
    """Load a workflow from a JSON file."""
    command = f"comphy-ui load_workflow {workflow_file}"
    run_command(command)

@click.command()
@click.argument('component')
def refresh_component(component):
    """Refresh a specific component in the Comphy UI."""
    command = f"comphy-ui refresh {component}"
    run_command(command)

@click.command()
@click.argument('image_file')
def load_from_image(image_file):
    """Load a full workflow from a generated image file (PNG, WebP, FLAC)."""
    command = f"comphy-ui load_from_image {image_file}"
    run_command(command)

@click.command()
@click.argument('workflow_file')
def save_workflow(workflow_file):
    """Save the current workflow to a JSON file."""
    command = f"comphy-ui save_workflow {workflow_file}"
    run_command(command)

@click.command()
@click.argument('config_file')
def set_config(config_file):
    """Set the config file for model search paths."""
    command = f"comphy-ui set_config {config_file}"
    run_command(command)

@click.command()
@click.argument('command')
def run_custom(command):
    """Run a custom Comphy UI command."""
    run_command(command)

@click.command()
@click.argument('image_path')
@click.argument('target_aspect_ratio', type=float)
@click.argument('output_path')
def resize_image(image_path, target_aspect_ratio, output_path):
    """Resize an image to a specified aspect ratio."""
    change_aspect_ratio(image_path, target_aspect_ratio, output_path)
    click.echo(f"Image saved to {output_path}")

@click.command()
@click.argument('prompt')
@click.argument('resolution', type=str)
@click.argument('output_path')
def generate_image(prompt, resolution, output_path):
    """Generate an image based on a prompt and resolution."""
    width, height = map(int, resolution.split('x'))
    # Command to generate image using comfy-cli
    command = f"comfy generate --prompt \"{prompt}\" --width {width} --height {height} --output {output_path}"
    run_command(command)
    click.echo(f"Image generated and saved to {output_path}")

# Adding commands to the CLI group
cli.add_command(start_ui)
cli.add_command(stop_ui)
cli.add_command(status_ui)
cli.add_command(load_model)
cli.add_command(load_workflow)
cli.add_command(refresh_component)
cli.add_command(load_from_image)
cli.add_command(save_workflow)
cli.add_command(set_config)
cli.add_command(run_custom)
cli.add_command(resize_image)
cli.add_command(generate_image)

if __name__ == "__main__":
    cli()
