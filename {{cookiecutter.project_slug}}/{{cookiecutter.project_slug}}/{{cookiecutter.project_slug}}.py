"""Main module."""
{% if cookiecutter.use_metaflow == 'y' -%}
from metaflow import FlowSpec, step{% endif %}

{% if cookiecutter.use_argparse == 'y' -%}
import argparse
import os{% endif %}


{% if cookiecutter.use_argparse == 'y' -%}
def main(main_args):
  parser = argparse.ArgumentParser(description="main")
  parser.add_argument("--arg1", required=True, help="...")
  args = parser.parse_args(main_args[1:]){% endif %}

{% if cookiecutter.use_metaflow == 'y' -%}
class {{ cookiecutter.project_slug }}(FlowSpec):
  """
  A flow to ...

  The flow performs the following steps:
  1) 
  ...
  n)
  """
  @step
  def start(self):
    """
    The start step:
    1)
    ...
    n)
    """
    self.next(self.some_step)

  @step
  def some_step(self):
    """
    Some step.
    """
    self.next(self.end)

  @step
  def end(self):
    """
    End the flow.
    """
    pass{% endif %}

if __name__ == '__main__':
  {% if cookiecutter.use_metaflow == 'y' -%}
  {{ cookiecutter.project_slug }}(){% endif %}

  {% if cookiecutter.use_argparse == 'y' -%}
  import sys
  sys.exit(main(sys.argv)){% endif %}
