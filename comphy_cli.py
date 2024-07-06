import click
import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        click.echo(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        click.echo(f"Error: {e.stderr.decode()}", err=True)

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

if __name__ == "__main__":
    cli()