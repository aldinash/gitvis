
# GitVis

GitVis is a tool that allows you to visualize your local commits for the last 6 months from a given date. The visualization is done in a manner similar to GitHub and GitLab, providing a familiar and intuitive interface.

The code is fully written in Python and is inspired by [gitcs](https://github.com/knbr13/gitcs).

## Demo
![gitvis](https://github.com/aldinash/gitvis/blob/main/gitvis.gif?raw=true)

Note that colors are highly dependent on the ANSI escape sequences of your terminal.

## Installations

The CLI is distributed via PyPi. To install the package:

```sh
pip install gitvis
```

Make sure to use virtual environments for better dependency management.

## Usage

The basic usage is straightforward. Simply run:

```sh
gitvis
```

GitVis will scan for `.git` folders in your current directory and use the global email for the contributions graph.

To run the tool with custom options, use the flags as shown below:

```sh
gitvis -d /home/user/directory --email example@email.com --since 01-14-2024
```

If you don't remember the flags, just run:

```sh
gitvis --help
```

## Future Plans

The project is still in its early stages, and it would be great to develop a tool that visualizes the entire Git workflow locally in the terminal. If you are interested in contributing to such tools, feel free to DM me.

## License

MIT