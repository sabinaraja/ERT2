/************* 
 * Ert2 *
 *************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.2.3.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'ERT2';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(WelcomeRoutineBegin());
flowScheduler.add(WelcomeRoutineEachFrame());
flowScheduler.add(WelcomeRoutineEnd());
flowScheduler.add(InstructionsRoutineBegin());
flowScheduler.add(InstructionsRoutineEachFrame());
flowScheduler.add(InstructionsRoutineEnd());
const practiceLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceLoopBegin(practiceLoopScheduler));
flowScheduler.add(practiceLoopScheduler);
flowScheduler.add(practiceLoopEnd);





flowScheduler.add(Instructions2RoutineBegin());
flowScheduler.add(Instructions2RoutineEachFrame());
flowScheduler.add(Instructions2RoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);





flowScheduler.add(EndMessageRoutineBegin());
flowScheduler.add(EndMessageRoutineEachFrame());
flowScheduler.add(EndMessageRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'Practice_Stimuli.xlsx', 'path': 'Practice_Stimuli.xlsx'},
    {'name': 'EmotionFace_Stimuli.xlsx', 'path': 'EmotionFace_Stimuli.xlsx'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.2.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var WelcomeClock;
var text_3;
var resources_2;
var InstructionsClock;
var text;
var key_resp;
var fixationcrossClock;
var text_7;
var PracticeFacesClock;
var practicefaces;
var BlankClock;
var PracticeResponseClock;
var text_6;
var sad;
var happy;
var fear;
var anger;
var surpise;
var disgust;
var mouse;
var Instructions2Clock;
var text_5;
var key_resp_3;
var FaceStimuliClock;
var FaceStimuli1;
var EmotionResponseClock;
var text_2;
var mouse_2;
var Surprise;
var Fear;
var Anger;
var Happy;
var Sad;
var Disgust;
var EndMessageClock;
var text_4;
var key_resp_2;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Welcome"
  WelcomeClock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'Welcome to Phase 2 of the Emotion Recognition Task!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  resources_2 = {
    status: PsychoJS.Status.NOT_STARTED
  };
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'In this task, you will see fixation cross followed by a photograph of an emotionally expressive face. Your task is to select the appropriate emotion from the labels presented on the screen: anger, disgust, happy, sad, surprise, or fear. \n\nPlease answer as quickly and as accurately as possible. You will begin with a set of practice trials before moving on to the real task.\n\nWhen you are ready to proceed, press any key to continue. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixationcross"
  fixationcrossClock = new util.Clock();
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: '+',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "PracticeFaces"
  PracticeFacesClock = new util.Clock();
  practicefaces = new visual.ImageStim({
    win : psychoJS.window,
    name : 'practicefaces', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.5, 0.65],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "Blank"
  BlankClock = new util.Clock();
  // Initialize components for Routine "PracticeResponse"
  PracticeResponseClock = new util.Clock();
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: 'Which emotion is the face displaying?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  sad = new visual.TextStim({
    win: psychoJS.window,
    name: 'sad',
    text: 'Sad',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.3, (- 0.2)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  happy = new visual.TextStim({
    win: psychoJS.window,
    name: 'happy',
    text: 'Happy',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.3), (- 0.2)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  fear = new visual.TextStim({
    win: psychoJS.window,
    name: 'fear',
    text: 'Fear',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.1), (- 0.2)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  anger = new visual.TextStim({
    win: psychoJS.window,
    name: 'anger',
    text: 'Anger',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.1, (- 0.2)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  surpise = new visual.TextStim({
    win: psychoJS.window,
    name: 'surpise',
    text: 'Surprise',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.5), (- 0.2)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  disgust = new visual.TextStim({
    win: psychoJS.window,
    name: 'disgust',
    text: 'Disgust',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.5, (- 0.2)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  // Initialize components for Routine "Instructions2"
  Instructions2Clock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "FaceStimuli"
  FaceStimuliClock = new util.Clock();
  FaceStimuli1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'FaceStimuli1', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.5, 0.65],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "EmotionResponse"
  EmotionResponseClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Which emotion is the face displaying?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  mouse_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_2.mouseClock = new util.Clock();
  Surprise = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'Surprise',
    text: 'Surprise',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [(- 0.55), (- 0.2)],
    letterHeight: 0.02,
    size: [0.2, 0.15],
    depth: -3
  });
  Surprise.clock = new util.Clock();
  
  Fear = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'Fear',
    text: 'Fear',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [(- 0.3), (- 0.2)],
    letterHeight: 0.02,
    size: [0.15, 0.15],
    depth: -4
  });
  Fear.clock = new util.Clock();
  
  Anger = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'Anger',
    text: 'Anger',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [(- 0.1), (- 0.2)],
    letterHeight: 0.02,
    size: [0.15, 0.15],
    depth: -5
  });
  Anger.clock = new util.Clock();
  
  Happy = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'Happy',
    text: 'Happy',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0.1, (- 0.2)],
    letterHeight: 0.02,
    size: [0.15, 0.15],
    depth: -6
  });
  Happy.clock = new util.Clock();
  
  Sad = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'Sad',
    text: 'Sad',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0.3, (- 0.2)],
    letterHeight: 0.02,
    size: [0.15, 0.15],
    depth: -7
  });
  Sad.clock = new util.Clock();
  
  Disgust = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'Disgust',
    text: 'Disgust',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0.45, (- 0.2)],
    letterHeight: 0.02,
    size: [0.2, 0.15],
    depth: -8
  });
  Disgust.clock = new util.Clock();
  
  // Initialize components for Routine "EndMessage"
  EndMessageClock = new util.Clock();
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'End of Task.\n\nYou may now press any key to terminate this window. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var WelcomeComponents;
function WelcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Welcome' ---
    t = 0;
    WelcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Welcome.started', globalClock.getTime());
    // keep track of which components have finished
    WelcomeComponents = [];
    WelcomeComponents.push(text_3);
    WelcomeComponents.push(resources_2);
    
    for (const thisComponent of WelcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function WelcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Welcome' ---
    // get current time
    t = WelcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // is it time to end the Routine? (based on local clock)
    if (t > 3.0) {
        continueRoutine = false
    }
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_3.setAutoDraw(false);
    }
    // start downloading resources specified by component resources_2
    if (t >= 0 && resources_2.status === PsychoJS.Status.NOT_STARTED) {
      console.log('register and start downloading resources specified by component resources_2');
      await psychoJS.serverManager.prepareResources(['index.html', 'Practice_Stimuli.xlsx', 'EmotionFace_Stimuli.xlsx', 'Practice/010_y_f_s_a.jpg', 'Practice/013_y_m_n_a.jpg', 'Practice/022_y_f_s_b.jpg', 'Practice/031_y_m_f_a.jpg', 'Practice/090_y_f_a_b.jpg', 'Practice/175_y_m_f_a.jpg', 'Trustworthiness/008_y_m_a_b.jpg', 'Trustworthiness/008_y_m_f_b.jpg', 'Trustworthiness/008_y_m_h_b.jpg', 'Trustworthiness/008_y_m_n_b.jpg', 'Trustworthiness/008_y_m_s_b.jpg', 'Trustworthiness/016_y_m_a_b.jpg', 'Trustworthiness/016_y_m_f_b.jpg', 'Trustworthiness/016_y_m_h_b.jpg', 'Trustworthiness/016_y_m_n_b.jpg', 'Trustworthiness/016_y_m_s_b.jpg', 'Trustworthiness/020_y_f_a_a.jpg', 'Trustworthiness/020_y_f_f_a.jpg', 'Trustworthiness/020_y_f_h_a.jpg', 'Trustworthiness/020_y_f_n_a.jpg', 'Trustworthiness/020_y_f_s_a.jpg', 'Trustworthiness/022_y_f_a_b.jpg', 'Trustworthiness/022_y_f_f_b.jpg', 'Trustworthiness/022_y_f_h_b.jpg', 'Trustworthiness/022_y_f_n_b.jpg', 'Trustworthiness/022_y_f_s_b.jpg', 'Trustworthiness/028_y_f_a_a.jpg', 'Trustworthiness/028_y_f_f_a.jpg', 'Trustworthiness/028_y_f_h_a.jpg', 'Trustworthiness/028_y_f_n_a.jpg', 'Trustworthiness/028_y_f_s_a.jpg', 'Trustworthiness/034_y_f_a_a.jpg', 'Trustworthiness/034_y_f_f_a.jpg', 'Trustworthiness/034_y_f_h_a.jpg', 'Trustworthiness/034_y_f_n_a.jpg', 'Trustworthiness/034_y_f_s_a.jpg', 'Trustworthiness/041_y_m_a_b.jpg', 'Trustworthiness/041_y_m_f_b.jpg', 'Trustworthiness/041_y_m_h_b.jpg', 'Trustworthiness/041_y_m_n_b.jpg', 'Trustworthiness/041_y_m_s_b.jpg', 'Trustworthiness/048_y_f_a_a.jpg', 'Trustworthiness/048_y_f_f_a.jpg', 'Trustworthiness/048_y_f_h_a.jpg', 'Trustworthiness/048_y_f_n_a.jpg', 'Trustworthiness/048_y_f_s_a.jpg', 'Trustworthiness/057_y_m_a_a.jpg', 'Trustworthiness/057_y_m_f_a.jpg', 'Trustworthiness/057_y_m_h_a.jpg', 'Trustworthiness/057_y_m_n_a.jpg', 'Trustworthiness/057_y_m_s_a.jpg', 'Trustworthiness/066_y_m_a_a.jpg', 'Trustworthiness/066_y_m_f_a.jpg', 'Trustworthiness/066_y_m_h_a.jpg', 'Trustworthiness/066_y_m_n_a.jpg', 'Trustworthiness/066_y_m_s_a.jpg', 'Trustworthiness/069_y_f_a_b.jpg', 'Trustworthiness/069_y_f_f_b.jpg', 'Trustworthiness/069_y_f_h_b.jpg', 'Trustworthiness/069_y_f_n_b.jpg', 'Trustworthiness/069_y_f_s_b.jpg', 'Trustworthiness/081_y_m_a_a.jpg', 'Trustworthiness/081_y_m_f_a.jpg', 'Trustworthiness/081_y_m_h_a.jpg', 'Trustworthiness/081_y_m_n_a.jpg', 'Trustworthiness/081_y_m_s_a.jpg', 'Trustworthiness/098_y_f_a_b.jpg', 'Trustworthiness/098_y_f_f_b.jpg', 'Trustworthiness/098_y_f_h_b.jpg', 'Trustworthiness/098_y_f_n_b.jpg', 'Trustworthiness/098_y_f_s_b.jpg', 'Trustworthiness/101_y_f_a_a.jpg', 'Trustworthiness/101_y_f_f_a.jpg', 'Trustworthiness/101_y_f_h_a.jpg', 'Trustworthiness/101_y_f_n_a.jpg', 'Trustworthiness/101_y_f_s_a.jpg', 'Trustworthiness/115_y_f_a_b.jpg', 'Trustworthiness/115_y_f_f_b.jpg', 'Trustworthiness/115_y_f_h_b.jpg', 'Trustworthiness/115_y_f_n_b.jpg', 'Trustworthiness/115_y_f_s_b.jpg', 'Trustworthiness/119_y_m_a_b.jpg', 'Trustworthiness/119_y_m_f_b.jpg', 'Trustworthiness/119_y_m_h_b.jpg', 'Trustworthiness/119_y_m_n_b.jpg', 'Trustworthiness/119_y_m_s_b.jpg', 'Trustworthiness/123_y_m_a_a.jpg', 'Trustworthiness/123_y_m_f_a.jpg', 'Trustworthiness/123_y_m_h_a.jpg', 'Trustworthiness/123_y_m_n_a.jpg', 'Trustworthiness/123_y_m_s_a.jpg', 'Trustworthiness/132_y_f_a_a.jpg', 'Trustworthiness/132_y_f_f_a.jpg', 'Trustworthiness/132_y_f_h_a.jpg', 'Trustworthiness/132_y_f_n_a.jpg', 'Trustworthiness/132_y_f_s_a.jpg', 'Trustworthiness/144_y_m_a_a.jpg', 'Trustworthiness/144_y_m_f_a.jpg', 'Trustworthiness/144_y_m_h_a.jpg', 'Trustworthiness/144_y_m_n_a.jpg', 'Trustworthiness/144_y_m_s_a.jpg', 'Trustworthiness/160_y_m_a_b.jpg', 'Trustworthiness/160_y_m_f_b.jpg', 'Trustworthiness/160_y_m_h_b.jpg', 'Trustworthiness/160_y_m_n_b.jpg', 'Trustworthiness/160_y_m_s_b.jpg', 'Trustworthiness/162_y_f_a_a.jpg', 'Trustworthiness/162_y_f_f_a.jpg', 'Trustworthiness/162_y_f_h_a.jpg', 'Trustworthiness/162_y_f_n_a.jpg', 'Trustworthiness/162_y_f_s_a.jpg', 'Trustworthiness/167_y_m_a_b.jpg', 'Trustworthiness/167_y_m_f_b.jpg', 'Trustworthiness/167_y_m_h_b.jpg', 'Trustworthiness/167_y_m_n_b.jpg', 'Trustworthiness/167_y_m_s_b.jpg', 'Trustworthiness/175_y_m_a_a.jpg', 'Trustworthiness/175_y_m_f_a.jpg', 'Trustworthiness/175_y_m_h_a.jpg', 'Trustworthiness/175_y_m_n_a.jpg', 'Trustworthiness/175_y_m_s_a.jpg', 'Trustworthiness/182_y_f_a_a.jpg', 'Trustworthiness/182_y_f_f_a.jpg', 'Trustworthiness/182_y_f_h_a.jpg', 'Trustworthiness/182_y_f_n_a.jpg', 'Trustworthiness/182_y_f_s_a.jpg']);
      resources_2.status = PsychoJS.Status.STARTED;
    }
    // check on the resources specified by component resources_2
    if (t >= null && resources_2.status === PsychoJS.Status.STARTED) {
      if (psychoJS.serverManager.getResourceStatus(['index.html', 'Practice_Stimuli.xlsx', 'EmotionFace_Stimuli.xlsx', 'Practice/010_y_f_s_a.jpg', 'Practice/013_y_m_n_a.jpg', 'Practice/022_y_f_s_b.jpg', 'Practice/031_y_m_f_a.jpg', 'Practice/090_y_f_a_b.jpg', 'Practice/175_y_m_f_a.jpg', 'Trustworthiness/008_y_m_a_b.jpg', 'Trustworthiness/008_y_m_f_b.jpg', 'Trustworthiness/008_y_m_h_b.jpg', 'Trustworthiness/008_y_m_n_b.jpg', 'Trustworthiness/008_y_m_s_b.jpg', 'Trustworthiness/016_y_m_a_b.jpg', 'Trustworthiness/016_y_m_f_b.jpg', 'Trustworthiness/016_y_m_h_b.jpg', 'Trustworthiness/016_y_m_n_b.jpg', 'Trustworthiness/016_y_m_s_b.jpg', 'Trustworthiness/020_y_f_a_a.jpg', 'Trustworthiness/020_y_f_f_a.jpg', 'Trustworthiness/020_y_f_h_a.jpg', 'Trustworthiness/020_y_f_n_a.jpg', 'Trustworthiness/020_y_f_s_a.jpg', 'Trustworthiness/022_y_f_a_b.jpg', 'Trustworthiness/022_y_f_f_b.jpg', 'Trustworthiness/022_y_f_h_b.jpg', 'Trustworthiness/022_y_f_n_b.jpg', 'Trustworthiness/022_y_f_s_b.jpg', 'Trustworthiness/028_y_f_a_a.jpg', 'Trustworthiness/028_y_f_f_a.jpg', 'Trustworthiness/028_y_f_h_a.jpg', 'Trustworthiness/028_y_f_n_a.jpg', 'Trustworthiness/028_y_f_s_a.jpg', 'Trustworthiness/034_y_f_a_a.jpg', 'Trustworthiness/034_y_f_f_a.jpg', 'Trustworthiness/034_y_f_h_a.jpg', 'Trustworthiness/034_y_f_n_a.jpg', 'Trustworthiness/034_y_f_s_a.jpg', 'Trustworthiness/041_y_m_a_b.jpg', 'Trustworthiness/041_y_m_f_b.jpg', 'Trustworthiness/041_y_m_h_b.jpg', 'Trustworthiness/041_y_m_n_b.jpg', 'Trustworthiness/041_y_m_s_b.jpg', 'Trustworthiness/048_y_f_a_a.jpg', 'Trustworthiness/048_y_f_f_a.jpg', 'Trustworthiness/048_y_f_h_a.jpg', 'Trustworthiness/048_y_f_n_a.jpg', 'Trustworthiness/048_y_f_s_a.jpg', 'Trustworthiness/057_y_m_a_a.jpg', 'Trustworthiness/057_y_m_f_a.jpg', 'Trustworthiness/057_y_m_h_a.jpg', 'Trustworthiness/057_y_m_n_a.jpg', 'Trustworthiness/057_y_m_s_a.jpg', 'Trustworthiness/066_y_m_a_a.jpg', 'Trustworthiness/066_y_m_f_a.jpg', 'Trustworthiness/066_y_m_h_a.jpg', 'Trustworthiness/066_y_m_n_a.jpg', 'Trustworthiness/066_y_m_s_a.jpg', 'Trustworthiness/069_y_f_a_b.jpg', 'Trustworthiness/069_y_f_f_b.jpg', 'Trustworthiness/069_y_f_h_b.jpg', 'Trustworthiness/069_y_f_n_b.jpg', 'Trustworthiness/069_y_f_s_b.jpg', 'Trustworthiness/081_y_m_a_a.jpg', 'Trustworthiness/081_y_m_f_a.jpg', 'Trustworthiness/081_y_m_h_a.jpg', 'Trustworthiness/081_y_m_n_a.jpg', 'Trustworthiness/081_y_m_s_a.jpg', 'Trustworthiness/098_y_f_a_b.jpg', 'Trustworthiness/098_y_f_f_b.jpg', 'Trustworthiness/098_y_f_h_b.jpg', 'Trustworthiness/098_y_f_n_b.jpg', 'Trustworthiness/098_y_f_s_b.jpg', 'Trustworthiness/101_y_f_a_a.jpg', 'Trustworthiness/101_y_f_f_a.jpg', 'Trustworthiness/101_y_f_h_a.jpg', 'Trustworthiness/101_y_f_n_a.jpg', 'Trustworthiness/101_y_f_s_a.jpg', 'Trustworthiness/115_y_f_a_b.jpg', 'Trustworthiness/115_y_f_f_b.jpg', 'Trustworthiness/115_y_f_h_b.jpg', 'Trustworthiness/115_y_f_n_b.jpg', 'Trustworthiness/115_y_f_s_b.jpg', 'Trustworthiness/119_y_m_a_b.jpg', 'Trustworthiness/119_y_m_f_b.jpg', 'Trustworthiness/119_y_m_h_b.jpg', 'Trustworthiness/119_y_m_n_b.jpg', 'Trustworthiness/119_y_m_s_b.jpg', 'Trustworthiness/123_y_m_a_a.jpg', 'Trustworthiness/123_y_m_f_a.jpg', 'Trustworthiness/123_y_m_h_a.jpg', 'Trustworthiness/123_y_m_n_a.jpg', 'Trustworthiness/123_y_m_s_a.jpg', 'Trustworthiness/132_y_f_a_a.jpg', 'Trustworthiness/132_y_f_f_a.jpg', 'Trustworthiness/132_y_f_h_a.jpg', 'Trustworthiness/132_y_f_n_a.jpg', 'Trustworthiness/132_y_f_s_a.jpg', 'Trustworthiness/144_y_m_a_a.jpg', 'Trustworthiness/144_y_m_f_a.jpg', 'Trustworthiness/144_y_m_h_a.jpg', 'Trustworthiness/144_y_m_n_a.jpg', 'Trustworthiness/144_y_m_s_a.jpg', 'Trustworthiness/160_y_m_a_b.jpg', 'Trustworthiness/160_y_m_f_b.jpg', 'Trustworthiness/160_y_m_h_b.jpg', 'Trustworthiness/160_y_m_n_b.jpg', 'Trustworthiness/160_y_m_s_b.jpg', 'Trustworthiness/162_y_f_a_a.jpg', 'Trustworthiness/162_y_f_f_a.jpg', 'Trustworthiness/162_y_f_h_a.jpg', 'Trustworthiness/162_y_f_n_a.jpg', 'Trustworthiness/162_y_f_s_a.jpg', 'Trustworthiness/167_y_m_a_b.jpg', 'Trustworthiness/167_y_m_f_b.jpg', 'Trustworthiness/167_y_m_h_b.jpg', 'Trustworthiness/167_y_m_n_b.jpg', 'Trustworthiness/167_y_m_s_b.jpg', 'Trustworthiness/175_y_m_a_a.jpg', 'Trustworthiness/175_y_m_f_a.jpg', 'Trustworthiness/175_y_m_h_a.jpg', 'Trustworthiness/175_y_m_n_a.jpg', 'Trustworthiness/175_y_m_s_a.jpg', 'Trustworthiness/182_y_f_a_a.jpg', 'Trustworthiness/182_y_f_f_a.jpg', 'Trustworthiness/182_y_f_h_a.jpg', 'Trustworthiness/182_y_f_n_a.jpg', 'Trustworthiness/182_y_f_s_a.jpg']) === core.ServerManager.ResourceStatus.DOWNLOADED) {
        console.log('finished downloading resources specified by component resources_2');
        resources_2.status = PsychoJS.Status.FINISHED;
      } else {
        console.log('resource specified in resources_2 took longer than expected to download');
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of WelcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function WelcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Welcome' ---
    for (const thisComponent of WelcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Welcome.stopped', globalClock.getTime());
    // the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_allKeys;
var InstructionsComponents;
function InstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instructions' ---
    t = 0;
    InstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Instructions.started', globalClock.getTime());
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    InstructionsComponents = [];
    InstructionsComponents.push(text);
    InstructionsComponents.push(key_resp);
    
    for (const thisComponent of InstructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instructions' ---
    // get current time
    t = InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: [], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instructions' ---
    for (const thisComponent of InstructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice;
function practiceLoopBegin(practiceLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practice = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Practice_Stimuli.xlsx',
      seed: undefined, name: 'practice'
    });
    psychoJS.experiment.addLoop(practice); // add the loop to the experiment
    currentLoop = practice;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPractice of practice) {
      snapshot = practice.getSnapshot();
      practiceLoopScheduler.add(importConditions(snapshot));
      practiceLoopScheduler.add(fixationcrossRoutineBegin(snapshot));
      practiceLoopScheduler.add(fixationcrossRoutineEachFrame());
      practiceLoopScheduler.add(fixationcrossRoutineEnd(snapshot));
      practiceLoopScheduler.add(PracticeFacesRoutineBegin(snapshot));
      practiceLoopScheduler.add(PracticeFacesRoutineEachFrame());
      practiceLoopScheduler.add(PracticeFacesRoutineEnd(snapshot));
      practiceLoopScheduler.add(BlankRoutineBegin(snapshot));
      practiceLoopScheduler.add(BlankRoutineEachFrame());
      practiceLoopScheduler.add(BlankRoutineEnd(snapshot));
      practiceLoopScheduler.add(PracticeResponseRoutineBegin(snapshot));
      practiceLoopScheduler.add(PracticeResponseRoutineEachFrame());
      practiceLoopScheduler.add(PracticeResponseRoutineEnd(snapshot));
      practiceLoopScheduler.add(practiceLoopEndIteration(practiceLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function practiceLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practice);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practiceLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'EmotionFace_Stimuli.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(fixationcrossRoutineBegin(snapshot));
      trialsLoopScheduler.add(fixationcrossRoutineEachFrame());
      trialsLoopScheduler.add(fixationcrossRoutineEnd(snapshot));
      trialsLoopScheduler.add(FaceStimuliRoutineBegin(snapshot));
      trialsLoopScheduler.add(FaceStimuliRoutineEachFrame());
      trialsLoopScheduler.add(FaceStimuliRoutineEnd(snapshot));
      trialsLoopScheduler.add(BlankRoutineBegin(snapshot));
      trialsLoopScheduler.add(BlankRoutineEachFrame());
      trialsLoopScheduler.add(BlankRoutineEnd(snapshot));
      trialsLoopScheduler.add(EmotionResponseRoutineBegin(snapshot));
      trialsLoopScheduler.add(EmotionResponseRoutineEachFrame());
      trialsLoopScheduler.add(EmotionResponseRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var fixationcrossComponents;
function fixationcrossRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixationcross' ---
    t = 0;
    fixationcrossClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('fixationcross.started', globalClock.getTime());
    // keep track of which components have finished
    fixationcrossComponents = [];
    fixationcrossComponents.push(text_7);
    
    for (const thisComponent of fixationcrossComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function fixationcrossRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixationcross' ---
    // get current time
    t = fixationcrossClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_7* updates
    if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_7.tStart = t;  // (not accounting for frame time here)
      text_7.frameNStart = frameN;  // exact frame index
      
      text_7.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_7.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fixationcrossComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixationcrossRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixationcross' ---
    for (const thisComponent of fixationcrossComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('fixationcross.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var PracticeFacesComponents;
function PracticeFacesRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PracticeFaces' ---
    t = 0;
    PracticeFacesClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.300000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('PracticeFaces.started', globalClock.getTime());
    practicefaces.setImage(Practice_Faces);
    // keep track of which components have finished
    PracticeFacesComponents = [];
    PracticeFacesComponents.push(practicefaces);
    
    for (const thisComponent of PracticeFacesComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function PracticeFacesRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PracticeFaces' ---
    // get current time
    t = PracticeFacesClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practicefaces* updates
    if (t >= 0.0 && practicefaces.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practicefaces.tStart = t;  // (not accounting for frame time here)
      practicefaces.frameNStart = frameN;  // exact frame index
      
      practicefaces.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (practicefaces.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practicefaces.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PracticeFacesComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PracticeFacesRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PracticeFaces' ---
    for (const thisComponent of PracticeFacesComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('PracticeFaces.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var BlankComponents;
function BlankRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Blank' ---
    t = 0;
    BlankClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Blank.started', globalClock.getTime());
    // keep track of which components have finished
    BlankComponents = [];
    
    for (const thisComponent of BlankComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function BlankRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Blank' ---
    // get current time
    t = BlankClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // is it time to end the Routine? (based on local clock)
    if (t > 0.5) {
        continueRoutine = false
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of BlankComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function BlankRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Blank' ---
    for (const thisComponent of BlankComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Blank.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var gotValidClick;
var PracticeResponseComponents;
function PracticeResponseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PracticeResponse' ---
    t = 0;
    PracticeResponseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('PracticeResponse.started', globalClock.getTime());
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from code_2
    if ((gotValidClick === true)) {
        (continueRoutine === true);
    }
    
    // keep track of which components have finished
    PracticeResponseComponents = [];
    PracticeResponseComponents.push(text_6);
    PracticeResponseComponents.push(sad);
    PracticeResponseComponents.push(happy);
    PracticeResponseComponents.push(fear);
    PracticeResponseComponents.push(anger);
    PracticeResponseComponents.push(surpise);
    PracticeResponseComponents.push(disgust);
    PracticeResponseComponents.push(mouse);
    
    for (const thisComponent of PracticeResponseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function PracticeResponseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PracticeResponse' ---
    // get current time
    t = PracticeResponseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_6* updates
    if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }
    
    
    // *sad* updates
    if (t >= 0.0 && sad.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sad.tStart = t;  // (not accounting for frame time here)
      sad.frameNStart = frameN;  // exact frame index
      
      sad.setAutoDraw(true);
    }
    
    
    // *happy* updates
    if (t >= 0.0 && happy.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      happy.tStart = t;  // (not accounting for frame time here)
      happy.frameNStart = frameN;  // exact frame index
      
      happy.setAutoDraw(true);
    }
    
    
    // *fear* updates
    if (t >= 0.0 && fear.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fear.tStart = t;  // (not accounting for frame time here)
      fear.frameNStart = frameN;  // exact frame index
      
      fear.setAutoDraw(true);
    }
    
    
    // *anger* updates
    if (t >= 0.0 && anger.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      anger.tStart = t;  // (not accounting for frame time here)
      anger.frameNStart = frameN;  // exact frame index
      
      anger.setAutoDraw(true);
    }
    
    
    // *surpise* updates
    if (t >= 0.0 && surpise.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      surpise.tStart = t;  // (not accounting for frame time here)
      surpise.frameNStart = frameN;  // exact frame index
      
      surpise.setAutoDraw(true);
    }
    
    
    // *disgust* updates
    if (t >= 0.0 && disgust.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      disgust.tStart = t;  // (not accounting for frame time here)
      disgust.frameNStart = frameN;  // exact frame index
      
      disgust.setAutoDraw(true);
    }
    
    // *mouse* updates
    if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = [0, 0, 0];  // if now button is down we will treat as 'new' click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse.getPos();
          mouse.x.push(_mouseXYs[0]);
          mouse.y.push(_mouseXYs[1]);
          mouse.leftButton.push(_mouseButtons[0]);
          mouse.midButton.push(_mouseButtons[1]);
          mouse.rightButton.push(_mouseButtons[2]);
          mouse.time.push(mouse.mouseClock.getTime());
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PracticeResponseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PracticeResponseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PracticeResponse' ---
    for (const thisComponent of PracticeResponseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('PracticeResponse.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse.x) {  psychoJS.experiment.addData('mouse.x', mouse.x[0])};
    if (mouse.y) {  psychoJS.experiment.addData('mouse.y', mouse.y[0])};
    if (mouse.leftButton) {  psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton[0])};
    if (mouse.midButton) {  psychoJS.experiment.addData('mouse.midButton', mouse.midButton[0])};
    if (mouse.rightButton) {  psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton[0])};
    if (mouse.time) {  psychoJS.experiment.addData('mouse.time', mouse.time[0])};
    
    // the Routine "PracticeResponse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_3_allKeys;
var Instructions2Components;
function Instructions2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instructions2' ---
    t = 0;
    Instructions2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Instructions2.started', globalClock.getTime());
    text_5.setText('The practice trials are now complete. The real task trials will now begin.\n\nWhen you are ready, press any key to continue. The first trial will begin immediately.');
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    Instructions2Components = [];
    Instructions2Components.push(text_5);
    Instructions2Components.push(key_resp_3);
    
    for (const thisComponent of Instructions2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Instructions2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instructions2' ---
    // get current time
    t = Instructions2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }
    
    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }
    
    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: [], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        key_resp_3.duration = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instructions2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instructions2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instructions2' ---
    for (const thisComponent of Instructions2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Instructions2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        psychoJS.experiment.addData('key_resp_3.duration', key_resp_3.duration);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "Instructions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var FaceStimuliComponents;
function FaceStimuliRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'FaceStimuli' ---
    t = 0;
    FaceStimuliClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.300000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('FaceStimuli.started', globalClock.getTime());
    FaceStimuli1.setImage(EmotionFace_Stimuli);
    // keep track of which components have finished
    FaceStimuliComponents = [];
    FaceStimuliComponents.push(FaceStimuli1);
    
    for (const thisComponent of FaceStimuliComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FaceStimuliRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'FaceStimuli' ---
    // get current time
    t = FaceStimuliClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *FaceStimuli1* updates
    if (t >= 0.0 && FaceStimuli1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      FaceStimuli1.tStart = t;  // (not accounting for frame time here)
      FaceStimuli1.frameNStart = frameN;  // exact frame index
      
      FaceStimuli1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (FaceStimuli1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      FaceStimuli1.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FaceStimuliComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FaceStimuliRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'FaceStimuli' ---
    for (const thisComponent of FaceStimuliComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('FaceStimuli.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var EmotionResponseComponents;
function EmotionResponseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'EmotionResponse' ---
    t = 0;
    EmotionResponseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('EmotionResponse.started', globalClock.getTime());
    // setup some python lists for storing info about the mouse_2
    // current position of the mouse:
    mouse_2.x = [];
    mouse_2.y = [];
    mouse_2.leftButton = [];
    mouse_2.midButton = [];
    mouse_2.rightButton = [];
    mouse_2.time = [];
    mouse_2.corr = [];
    mouse_2.clicked_name = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from code
    if ((Correct_Answer === "none")) {
        continueRoutine = true;
    } else {
        continueRoutine = true;
    }
    if ((gotValidClick === true)) {
        (continueRoutine === true);
    }
    
    // reset Surprise to account for continued clicks & clear times on/off
    Surprise.reset()
    // reset Fear to account for continued clicks & clear times on/off
    Fear.reset()
    // reset Anger to account for continued clicks & clear times on/off
    Anger.reset()
    // reset Happy to account for continued clicks & clear times on/off
    Happy.reset()
    // reset Sad to account for continued clicks & clear times on/off
    Sad.reset()
    // reset Disgust to account for continued clicks & clear times on/off
    Disgust.reset()
    // keep track of which components have finished
    EmotionResponseComponents = [];
    EmotionResponseComponents.push(text_2);
    EmotionResponseComponents.push(mouse_2);
    EmotionResponseComponents.push(Surprise);
    EmotionResponseComponents.push(Fear);
    EmotionResponseComponents.push(Anger);
    EmotionResponseComponents.push(Happy);
    EmotionResponseComponents.push(Sad);
    EmotionResponseComponents.push(Disgust);
    
    for (const thisComponent of EmotionResponseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var corr;
var corrAns;
function EmotionResponseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'EmotionResponse' ---
    // get current time
    t = EmotionResponseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }
    
    // *mouse_2* updates
    if (t >= 0.0 && mouse_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_2.tStart = t;  // (not accounting for frame time here)
      mouse_2.frameNStart = frameN;  // exact frame index
      
      mouse_2.status = PsychoJS.Status.STARTED;
      mouse_2.mouseClock.reset();
      prevButtonState = mouse_2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of ['Sad', 'Happy', 'Fear', 'Anger', 'Surprise', 'Disgust']) {
            if (obj.contains(mouse_2)) {
              gotValidClick = true;
              mouse_2.clicked_name.push(obj.name)
            }
          }
          // check whether click was in correct object
          if (gotValidClick) {
              corr = 0;
              corrAns = Correct_Answer;
              for (let obj of [corrAns]) {
                  if (obj.contains(mouse_2)) {
                      corr = 1;
                  };
              };
              mouse_2.corr.push(corr);
          };
          if (gotValidClick === true) { 
            _mouseXYs = mouse_2.getPos();
            mouse_2.x.push(_mouseXYs[0]);
            mouse_2.y.push(_mouseXYs[1]);
            mouse_2.leftButton.push(_mouseButtons[0]);
            mouse_2.midButton.push(_mouseButtons[1]);
            mouse_2.rightButton.push(_mouseButtons[2]);
            mouse_2.time.push(mouse_2.mouseClock.getTime());
          }
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *Surprise* updates
    if (t >= 0 && Surprise.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Surprise.tStart = t;  // (not accounting for frame time here)
      Surprise.frameNStart = frameN;  // exact frame index
      
      Surprise.setAutoDraw(true);
    }
    
    if (Surprise.status === PsychoJS.Status.STARTED) {
      // check whether Surprise has been pressed
      if (Surprise.isClicked) {
        if (!Surprise.wasClicked) {
          // store time of first click
          Surprise.timesOn.push(Surprise.clock.getTime());
          Surprise.numClicks += 1;
          // store time clicked until
          Surprise.timesOff.push(Surprise.clock.getTime());
        } else {
          // update time clicked until;
          Surprise.timesOff[Surprise.timesOff.length - 1] = Surprise.clock.getTime();
        }
        if (!Surprise.wasClicked) {
          // end routine when Surprise is clicked
          continueRoutine = false;
          
        }
        // if Surprise is still clicked next frame, it is not a new click
        Surprise.wasClicked = true;
      } else {
        // if Surprise is clicked next frame, it is a new click
        Surprise.wasClicked = false;
      }
    } else {
      // keep clock at 0 if Surprise hasn't started / has finished
      Surprise.clock.reset();
      // if Surprise is clicked next frame, it is a new click
      Surprise.wasClicked = false;
    }
    
    // *Fear* updates
    if (t >= 0 && Fear.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fear.tStart = t;  // (not accounting for frame time here)
      Fear.frameNStart = frameN;  // exact frame index
      
      Fear.setAutoDraw(true);
    }
    
    if (Fear.status === PsychoJS.Status.STARTED) {
      // check whether Fear has been pressed
      if (Fear.isClicked) {
        if (!Fear.wasClicked) {
          // store time of first click
          Fear.timesOn.push(Fear.clock.getTime());
          Fear.numClicks += 1;
          // store time clicked until
          Fear.timesOff.push(Fear.clock.getTime());
        } else {
          // update time clicked until;
          Fear.timesOff[Fear.timesOff.length - 1] = Fear.clock.getTime();
        }
        if (!Fear.wasClicked) {
          // end routine when Fear is clicked
          continueRoutine = false;
          
        }
        // if Fear is still clicked next frame, it is not a new click
        Fear.wasClicked = true;
      } else {
        // if Fear is clicked next frame, it is a new click
        Fear.wasClicked = false;
      }
    } else {
      // keep clock at 0 if Fear hasn't started / has finished
      Fear.clock.reset();
      // if Fear is clicked next frame, it is a new click
      Fear.wasClicked = false;
    }
    
    // *Anger* updates
    if (t >= 0 && Anger.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Anger.tStart = t;  // (not accounting for frame time here)
      Anger.frameNStart = frameN;  // exact frame index
      
      Anger.setAutoDraw(true);
    }
    
    if (Anger.status === PsychoJS.Status.STARTED) {
      // check whether Anger has been pressed
      if (Anger.isClicked) {
        if (!Anger.wasClicked) {
          // store time of first click
          Anger.timesOn.push(Anger.clock.getTime());
          Anger.numClicks += 1;
          // store time clicked until
          Anger.timesOff.push(Anger.clock.getTime());
        } else {
          // update time clicked until;
          Anger.timesOff[Anger.timesOff.length - 1] = Anger.clock.getTime();
        }
        if (!Anger.wasClicked) {
          // end routine when Anger is clicked
          continueRoutine = false;
          
        }
        // if Anger is still clicked next frame, it is not a new click
        Anger.wasClicked = true;
      } else {
        // if Anger is clicked next frame, it is a new click
        Anger.wasClicked = false;
      }
    } else {
      // keep clock at 0 if Anger hasn't started / has finished
      Anger.clock.reset();
      // if Anger is clicked next frame, it is a new click
      Anger.wasClicked = false;
    }
    
    // *Happy* updates
    if (t >= 0 && Happy.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Happy.tStart = t;  // (not accounting for frame time here)
      Happy.frameNStart = frameN;  // exact frame index
      
      Happy.setAutoDraw(true);
    }
    
    if (Happy.status === PsychoJS.Status.STARTED) {
      // check whether Happy has been pressed
      if (Happy.isClicked) {
        if (!Happy.wasClicked) {
          // store time of first click
          Happy.timesOn.push(Happy.clock.getTime());
          Happy.numClicks += 1;
          // store time clicked until
          Happy.timesOff.push(Happy.clock.getTime());
        } else {
          // update time clicked until;
          Happy.timesOff[Happy.timesOff.length - 1] = Happy.clock.getTime();
        }
        if (!Happy.wasClicked) {
          // end routine when Happy is clicked
          continueRoutine = false;
          
        }
        // if Happy is still clicked next frame, it is not a new click
        Happy.wasClicked = true;
      } else {
        // if Happy is clicked next frame, it is a new click
        Happy.wasClicked = false;
      }
    } else {
      // keep clock at 0 if Happy hasn't started / has finished
      Happy.clock.reset();
      // if Happy is clicked next frame, it is a new click
      Happy.wasClicked = false;
    }
    
    // *Sad* updates
    if (t >= 0 && Sad.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Sad.tStart = t;  // (not accounting for frame time here)
      Sad.frameNStart = frameN;  // exact frame index
      
      Sad.setAutoDraw(true);
    }
    
    if (Sad.status === PsychoJS.Status.STARTED) {
      // check whether Sad has been pressed
      if (Sad.isClicked) {
        if (!Sad.wasClicked) {
          // store time of first click
          Sad.timesOn.push(Sad.clock.getTime());
          Sad.numClicks += 1;
          // store time clicked until
          Sad.timesOff.push(Sad.clock.getTime());
        } else {
          // update time clicked until;
          Sad.timesOff[Sad.timesOff.length - 1] = Sad.clock.getTime();
        }
        if (!Sad.wasClicked) {
          // end routine when Sad is clicked
          continueRoutine = false;
          
        }
        // if Sad is still clicked next frame, it is not a new click
        Sad.wasClicked = true;
      } else {
        // if Sad is clicked next frame, it is a new click
        Sad.wasClicked = false;
      }
    } else {
      // keep clock at 0 if Sad hasn't started / has finished
      Sad.clock.reset();
      // if Sad is clicked next frame, it is a new click
      Sad.wasClicked = false;
    }
    
    // *Disgust* updates
    if (t >= 0 && Disgust.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Disgust.tStart = t;  // (not accounting for frame time here)
      Disgust.frameNStart = frameN;  // exact frame index
      
      Disgust.setAutoDraw(true);
    }
    
    if (Disgust.status === PsychoJS.Status.STARTED) {
      // check whether Disgust has been pressed
      if (Disgust.isClicked) {
        if (!Disgust.wasClicked) {
          // store time of first click
          Disgust.timesOn.push(Disgust.clock.getTime());
          Disgust.numClicks += 1;
          // store time clicked until
          Disgust.timesOff.push(Disgust.clock.getTime());
        } else {
          // update time clicked until;
          Disgust.timesOff[Disgust.timesOff.length - 1] = Disgust.clock.getTime();
        }
        if (!Disgust.wasClicked) {
          // end routine when Disgust is clicked
          continueRoutine = false;
          
        }
        // if Disgust is still clicked next frame, it is not a new click
        Disgust.wasClicked = true;
      } else {
        // if Disgust is clicked next frame, it is a new click
        Disgust.wasClicked = false;
      }
    } else {
      // keep clock at 0 if Disgust hasn't started / has finished
      Disgust.clock.reset();
      // if Disgust is clicked next frame, it is a new click
      Disgust.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EmotionResponseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EmotionResponseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'EmotionResponse' ---
    for (const thisComponent of EmotionResponseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('EmotionResponse.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_2.x) {  psychoJS.experiment.addData('mouse_2.x', mouse_2.x[0])};
    if (mouse_2.y) {  psychoJS.experiment.addData('mouse_2.y', mouse_2.y[0])};
    if (mouse_2.leftButton) {  psychoJS.experiment.addData('mouse_2.leftButton', mouse_2.leftButton[0])};
    if (mouse_2.midButton) {  psychoJS.experiment.addData('mouse_2.midButton', mouse_2.midButton[0])};
    if (mouse_2.rightButton) {  psychoJS.experiment.addData('mouse_2.rightButton', mouse_2.rightButton[0])};
    if (mouse_2.time) {  psychoJS.experiment.addData('mouse_2.time', mouse_2.time[0])};
    if (mouse_2.corr) {  psychoJS.experiment.addData('mouse_2.corr', mouse_2.corr[0])};
    if (mouse_2.clicked_name) {  psychoJS.experiment.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])};
    
    psychoJS.experiment.addData('Surprise.numClicks', Surprise.numClicks);
    psychoJS.experiment.addData('Surprise.timesOn', Surprise.timesOn);
    psychoJS.experiment.addData('Surprise.timesOff', Surprise.timesOff);
    psychoJS.experiment.addData('Fear.numClicks', Fear.numClicks);
    psychoJS.experiment.addData('Fear.timesOn', Fear.timesOn);
    psychoJS.experiment.addData('Fear.timesOff', Fear.timesOff);
    psychoJS.experiment.addData('Anger.numClicks', Anger.numClicks);
    psychoJS.experiment.addData('Anger.timesOn', Anger.timesOn);
    psychoJS.experiment.addData('Anger.timesOff', Anger.timesOff);
    psychoJS.experiment.addData('Happy.numClicks', Happy.numClicks);
    psychoJS.experiment.addData('Happy.timesOn', Happy.timesOn);
    psychoJS.experiment.addData('Happy.timesOff', Happy.timesOff);
    psychoJS.experiment.addData('Sad.numClicks', Sad.numClicks);
    psychoJS.experiment.addData('Sad.timesOn', Sad.timesOn);
    psychoJS.experiment.addData('Sad.timesOff', Sad.timesOff);
    psychoJS.experiment.addData('Disgust.numClicks', Disgust.numClicks);
    psychoJS.experiment.addData('Disgust.timesOn', Disgust.timesOn);
    psychoJS.experiment.addData('Disgust.timesOff', Disgust.timesOff);
    // the Routine "EmotionResponse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_2_allKeys;
var EndMessageComponents;
function EndMessageRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'EndMessage' ---
    t = 0;
    EndMessageClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('EndMessage.started', globalClock.getTime());
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    EndMessageComponents = [];
    EndMessageComponents.push(text_4);
    EndMessageComponents.push(key_resp_2);
    
    for (const thisComponent of EndMessageComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EndMessageRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'EndMessage' ---
    // get current time
    t = EndMessageClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }
    
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }
    
    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: [], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndMessageComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndMessageRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'EndMessage' ---
    for (const thisComponent of EndMessageComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('EndMessage.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "EndMessage" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
