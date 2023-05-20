from os import system
import platform


def beep(sec=1, freq=1000) -> None:
    """
    Make beep sound.

    :param sec: Beep duration in seconds (default is 1).
    :param freq: Beep frequency in Hz (default is 1000).
    """
    sys = platform.system()

    if sys == "Windows":
        import winsound

        winsound.Beep(int(1000 * sec), freq)
    else:
        system("play -nq -t alsa synth {} sine {}".format(sec, freq))
