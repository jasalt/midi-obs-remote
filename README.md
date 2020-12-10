GUI tool for controlling OBS sources remotely via MIDI events coming from Virtual MIDI or a midi device. 

Written with [Toga](https://github.com/beeware/toga/) GUI library, and [
obs-ws-rc](https://github.com/KirillMysnik/obs-ws-rc) utilising asyncio library.

# Use Cases
- Extending [Unzyme light show Ableton Live setup](https://unzyme.com/diy/ableton-live-dmx-controller/) (MIDI to DMX) for controlling livestream cameras.
- Activating music production livestream camera to show the keyboard when notes are pressed for [my own livestreaming](https://www.youtube.com/channel/UCTOUZMACD-mX_qTOziYLMxg) purposes.

# Roadmap
TODO Query and Select MIDI Device
TODO Mapping GUI layout
TODO Query Sources from OBS
TODO Message OBS to switch source

# Related projects
More advanced CLI only application https://github.com/lebaston100/MIDItoOBS for which someone did GUI with QT in some extent https://github.com/cpyarger/Midi2OBS-Configurator. Taking this as an example till some extent, but focusing on building a GUI from the get go with minimal set of featured for a couple specified use cases.