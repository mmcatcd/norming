window.AudioContext = window.AudioContext || window.webkitAudioContext;

let freqs = [];

const pitch = 440;
let octave = 4;
let temperament = "Equal temperament";

let context = new AudioContext();
const gainNode = context.createGain();
gainNode.gain.value = 0.2;
gainNode.connect(context.destination);

const changeOctave = (newOctave) => {
  octave = newOctave;
  playNotesWithOscillators();
}

const changeTemperament = (newTemperament) => {
  temperament = newTemperament;
  playNotesWithOscillators();
}

const notes = {
  "C": 0,
  "C#": 1,
  "D": 2,
  "D#": 3,
  "E": 4,
  "F": 5,
  "F#": 6,
  "G": 7,
  "G#": 8,
  "A": 9,
  "A#": 10,
  "B": 11,
  "C_": 12,
}

// pyt_ratio = np.asarray([1, 256/243, 9/8, 32/27, 81/64, 4/3, 729/512, 3/2, 128/81, 27/16, 16/9, 243/128, 2])

const notesPythag = {
  0: (32/27) / 2,
  1: (81/64) / 2,
  2: (4/3) / 2,
  3: (729/512) / 2,
  4: (3/2) / 2,
  5: (128/81) / 2,
  6: (27/16) / 2,
  7: (16/9) / 2,
  8: (243/128) / 2,
  9: 1/1,
  10: 256/243,
  11: 9/8,
  12: 32/27,
}

const noteStates = Array(13).fill(false);
const noteIdxToFreq = (noteIdx) => (pitch * Math.pow(2, ((noteIdx - notes["A"]) + (12 * (octave - 4))) / 12)).toFixed(3);

const noteIdxToFreqPythagoras = (noteIdx) => {
  const trueOctave = octave - 4;
  return pitch * notesPythag[noteIdx] * Math.pow(2, trueOctave);
}

const createOscillator = (ctx, freq) => {
  const osc = ctx.createOscillator();
  osc.type = 'sine';
  osc.frequency.value = freq;
  osc.connect(gainNode);
  osc.start();
  return osc;
}

const playNotesWithOscillators = () => {
  oscillators.forEach((oscillator) => {
    if (oscillator) {
      oscillator.disconnect();
    }
  });

  noteStates.forEach((noteState, noteIdx) => {
    if (noteState === true) {
      const freqFunc = temperament === "pythag" ? noteIdxToFreqPythagoras : noteIdxToFreq;
      console.log("Freq:", freqFunc(noteIdx));
      oscillators[noteIdx] = createOscillator(context, freqFunc(noteIdx));
    }
  });
}

const oscillators = Array(13).fill(null);

document.querySelectorAll(".note-button").forEach(
  (el) => el.addEventListener("click", (event) => {
  const noteIdx = notes[event.target.name];
  let noteState = noteStates[noteIdx];
  if (noteState === true) {
    event.target.className = event.target.className.replace(" active-note-button", "");
    oscillators[noteIdx].disconnect();
    oscillators[noteIdx] = null;
    noteStates[noteIdx] = false;
  } else {
    event.target.className += " active-note-button";
    // console.log("Freq:", noteIdxToFreqPythagoras(noteIdx));
    // oscillators[noteIdx] = createOscillator(context, noteIdxToFreqPythagoras(noteIdx));
    noteStates[noteIdx] = true;
    playNotesWithOscillators();
  }
}));
