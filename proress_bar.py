import colorama

def progress_bar(progress, total, color=colorama.Fore.YELLOW):
  """
    Display a progress bar in the terminal.

    Args:
        progress (int): The current progress value.
        total (int): The total value indicating completion.
        color (str, optional): The color code for the progress bar (default is colorama.Fore.YELLOW).

    Example:
        To display a yellow progress bar for 50% completion:
        >>> progress_bar(50, 100, color=colorama.Fore.YELLOW)

    Note:
        This function updates the progress bar in the terminal and provides a visual indication
        of the progress of a task.

    """
  
  percent = 100 * (progress / float(total))
  bar = '#' * int(percent) + '-' * (100 - int(percent))
  print(color + f"\r |{bar}| {percent:.2f}%", end="\r")

  if progress == total:
    print(colorama.Fore.GREEN + f"\r |{bar}| {percent:.2f}%", end="\r")