﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on Wed Jan 15 14:36:14 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'ERT2'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/sabina/Desktop/IN-PERSON STUDY/ERT2/ERT2_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=(1024, 768), fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Welcome" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='Welcome to Phase 2 of the Emotion Recognition Task!',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Instructions" ---
    text = visual.TextStim(win=win, name='text',
        text='In this task, you will see a fixation cross followed by a photograph of an emotionally expressive face. Your task is to select the appropriate emotion from the labels presented on the screen: angry, disgusted, happy, sad, surprised, or scared. \n\nPlease answer as quickly and as accurately as possible. You will begin with a set of practice trials before moving on to the real task.\n\nWhen you are ready to proceed, press any key to continue. ',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "fixationcross" ---
    text_7 = visual.TextStim(win=win, name='text_7',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.12, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "PracticeFaces" ---
    practicefaces = visual.ImageStim(
        win=win,
        name='practicefaces', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.65),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "Blank" ---
    
    # --- Initialize components for Routine "Response" ---
    text_6 = visual.TextStim(win=win, name='text_6',
        text='Which emotion is the face displaying?',
        font='Open Sans',
        pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    button1 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(-0.5, -0.2),
        letterHeight=0.02,
        size=(0.15, 0.15), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button1',
        depth=-2
    )
    button1.buttonClock = core.Clock()
    button2 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(-0.3, -0.2),
        letterHeight=0.02,
        size=(0.15, 0.15), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button2',
        depth=-3
    )
    button2.buttonClock = core.Clock()
    button3 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(-0.1, -0.2),
        letterHeight=0.02,
        size=(0.15, 0.15), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button3',
        depth=-4
    )
    button3.buttonClock = core.Clock()
    button4 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(0.1, -0.2),
        letterHeight=0.02,
        size=(0.15, 0.15), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button4',
        depth=-5
    )
    button4.buttonClock = core.Clock()
    button5 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(0.3, -0.2),
        letterHeight=0.02,
        size=(0.15, 0.15), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button5',
        depth=-6
    )
    button5.buttonClock = core.Clock()
    button6 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(0.5, -0.2),
        letterHeight=0.02,
        size=(0.15, 0.15), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button6',
        depth=-7
    )
    button6.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "Instructions2" ---
    text_5 = visual.TextStim(win=win, name='text_5',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_3 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "fixationcross" ---
    text_7 = visual.TextStim(win=win, name='text_7',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.12, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "FaceStimuli" ---
    FaceStimuli1 = visual.ImageStim(
        win=win,
        name='FaceStimuli1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.65),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "Blank" ---
    
    # --- Initialize components for Routine "Response" ---
    text_6 = visual.TextStim(win=win, name='text_6',
        text='Which emotion is the face displaying?',
        font='Open Sans',
        pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    button1 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(-0.5, -0.2),
        letterHeight=0.02,
        size=(0.15, 0.15), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button1',
        depth=-2
    )
    button1.buttonClock = core.Clock()
    button2 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(-0.3, -0.2),
        letterHeight=0.02,
        size=(0.15, 0.15), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button2',
        depth=-3
    )
    button2.buttonClock = core.Clock()
    button3 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(-0.1, -0.2),
        letterHeight=0.02,
        size=(0.15, 0.15), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button3',
        depth=-4
    )
    button3.buttonClock = core.Clock()
    button4 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(0.1, -0.2),
        letterHeight=0.02,
        size=(0.15, 0.15), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button4',
        depth=-5
    )
    button4.buttonClock = core.Clock()
    button5 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(0.3, -0.2),
        letterHeight=0.02,
        size=(0.15, 0.15), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button5',
        depth=-6
    )
    button5.buttonClock = core.Clock()
    button6 = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(0.5, -0.2),
        letterHeight=0.02,
        size=(0.15, 0.15), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button6',
        depth=-7
    )
    button6.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "EndMessage" ---
    text_4 = visual.TextStim(win=win, name='text_4',
        text='End of Task.\n\nYou may now press any key to terminate this window. ',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "Welcome" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Welcome.started', globalClock.getTime())
    # keep track of which components have finished
    WelcomeComponents = [text_3]
    for thisComponent in WelcomeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Welcome" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 3.0-frameTolerance:
            continueRoutine = False
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WelcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Welcome" ---
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Welcome.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # --- Prepare to start Routine "Instructions" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instructions.started', globalClock.getTime())
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    InstructionsComponents = [text, key_resp]
    for thisComponent in InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions" ---
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instructions.stopped', globalClock.getTime())
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Practice_Stimuli.xlsx'),
        seed=None, name='practice')
    thisExp.addLoop(practice)  # add the loop to the experiment
    thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            globals()[paramName] = thisPractice[paramName]
    
    for thisPractice in practice:
        currentLoop = practice
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
        if thisPractice != None:
            for paramName in thisPractice:
                globals()[paramName] = thisPractice[paramName]
        
        # --- Prepare to start Routine "fixationcross" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('fixationcross.started', globalClock.getTime())
        # keep track of which components have finished
        fixationcrossComponents = [text_7]
        for thisComponent in fixationcrossComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixationcross" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_7* updates
            
            # if text_7 is starting this frame...
            if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_7.frameNStart = frameN  # exact frame index
                text_7.tStart = t  # local t and not account for scr refresh
                text_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_7.status = STARTED
                text_7.setAutoDraw(True)
            
            # if text_7 is active this frame...
            if text_7.status == STARTED:
                # update params
                pass
            
            # if text_7 is stopping this frame...
            if text_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_7.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_7.tStop = t  # not accounting for scr refresh
                    text_7.frameNStop = frameN  # exact frame index
                    # update status
                    text_7.status = FINISHED
                    text_7.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationcrossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixationcross" ---
        for thisComponent in fixationcrossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('fixationcross.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "PracticeFaces" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('PracticeFaces.started', globalClock.getTime())
        practicefaces.setImage(Practice_Faces)
        # keep track of which components have finished
        PracticeFacesComponents = [practicefaces]
        for thisComponent in PracticeFacesComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "PracticeFaces" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.3:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practicefaces* updates
            
            # if practicefaces is starting this frame...
            if practicefaces.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practicefaces.frameNStart = frameN  # exact frame index
                practicefaces.tStart = t  # local t and not account for scr refresh
                practicefaces.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practicefaces, 'tStartRefresh')  # time at next scr refresh
                # update status
                practicefaces.status = STARTED
                practicefaces.setAutoDraw(True)
            
            # if practicefaces is active this frame...
            if practicefaces.status == STARTED:
                # update params
                pass
            
            # if practicefaces is stopping this frame...
            if practicefaces.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practicefaces.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    practicefaces.tStop = t  # not accounting for scr refresh
                    practicefaces.frameNStop = frameN  # exact frame index
                    # update status
                    practicefaces.status = FINISHED
                    practicefaces.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeFacesComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PracticeFaces" ---
        for thisComponent in PracticeFacesComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('PracticeFaces.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.300000)
        
        # --- Prepare to start Routine "Blank" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Blank.started', globalClock.getTime())
        # keep track of which components have finished
        BlankComponents = []
        for thisComponent in BlankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Blank" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > 0.5-frameTolerance:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BlankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Blank" ---
        for thisComponent in BlankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Blank.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "Response" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Response.started', globalClock.getTime())
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        button1.setText(button1.text)
        # reset button1 to account for continued clicks & clear times on/off
        button1.reset()
        button2.setText(button2.text)
        # reset button2 to account for continued clicks & clear times on/off
        button2.reset()
        button3.setText(button3.text)
        # reset button3 to account for continued clicks & clear times on/off
        button3.reset()
        button4.setText(button4.text)
        # reset button4 to account for continued clicks & clear times on/off
        button4.reset()
        button5.setText(button5.text)
        # reset button5 to account for continued clicks & clear times on/off
        button5.reset()
        button6.setText(button6.text)
        # reset button6 to account for continued clicks & clear times on/off
        button6.reset()
        # Run 'Begin Routine' code from code_3
        # Define the original list of emotions
        emotions = ["Happy", "Sad", "Surprised", "Angry", "Scared", "Disgusted"]
        
        # Randomize the order
        shuffled_emotions = emotions.copy()
        shuffle(shuffled_emotions)
        
        # Assign the randomized labels to the buttons
        button1.text = shuffled_emotions[0]
        button2.text = shuffled_emotions[1]
        button3.text = shuffled_emotions[2]
        button4.text = shuffled_emotions[3]
        button5.text = shuffled_emotions[4]
        button6.text = shuffled_emotions[5]
        
        # keep track of which components have finished
        ResponseComponents = [text_6, mouse, button1, button2, button3, button4, button5, button6]
        for thisComponent in ResponseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Response" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_6* updates
            
            # if text_6 is starting this frame...
            if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_6.status = STARTED
                text_6.setAutoDraw(True)
            
            # if text_6 is active this frame...
            if text_6.status == STARTED:
                # update params
                pass
            # *mouse* updates
            
            # if mouse is starting this frame...
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames(['button1', 'button2', 'button3', 'button4', 'button5', 'button6'], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            # *button1* updates
            
            # if button1 is starting this frame...
            if button1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button1.frameNStart = frameN  # exact frame index
                button1.tStart = t  # local t and not account for scr refresh
                button1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button1, 'tStartRefresh')  # time at next scr refresh
                # update status
                button1.status = STARTED
                button1.setAutoDraw(True)
            
            # if button1 is active this frame...
            if button1.status == STARTED:
                # update params
                pass
                # check whether button1 has been pressed
                if button1.isClicked:
                    if not button1.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button1.timesOn.append(button1.buttonClock.getTime())
                        button1.timesOff.append(button1.buttonClock.getTime())
                    elif len(button1.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button1.timesOff[-1] = button1.buttonClock.getTime()
                    if not button1.wasClicked:
                        # end routine when button1 is clicked
                        continueRoutine = False
                    if not button1.wasClicked:
                        # run callback code when button1 is clicked
                        pass
            # take note of whether button1 was clicked, so that next frame we know if clicks are new
            button1.wasClicked = button1.isClicked and button1.status == STARTED
            # *button2* updates
            
            # if button2 is starting this frame...
            if button2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button2.frameNStart = frameN  # exact frame index
                button2.tStart = t  # local t and not account for scr refresh
                button2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button2, 'tStartRefresh')  # time at next scr refresh
                # update status
                button2.status = STARTED
                button2.setAutoDraw(True)
            
            # if button2 is active this frame...
            if button2.status == STARTED:
                # update params
                pass
                # check whether button2 has been pressed
                if button2.isClicked:
                    if not button2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button2.timesOn.append(button2.buttonClock.getTime())
                        button2.timesOff.append(button2.buttonClock.getTime())
                    elif len(button2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button2.timesOff[-1] = button2.buttonClock.getTime()
                    if not button2.wasClicked:
                        # end routine when button2 is clicked
                        continueRoutine = False
                    if not button2.wasClicked:
                        # run callback code when button2 is clicked
                        pass
            # take note of whether button2 was clicked, so that next frame we know if clicks are new
            button2.wasClicked = button2.isClicked and button2.status == STARTED
            # *button3* updates
            
            # if button3 is starting this frame...
            if button3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button3.frameNStart = frameN  # exact frame index
                button3.tStart = t  # local t and not account for scr refresh
                button3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button3, 'tStartRefresh')  # time at next scr refresh
                # update status
                button3.status = STARTED
                button3.setAutoDraw(True)
            
            # if button3 is active this frame...
            if button3.status == STARTED:
                # update params
                pass
                # check whether button3 has been pressed
                if button3.isClicked:
                    if not button3.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button3.timesOn.append(button3.buttonClock.getTime())
                        button3.timesOff.append(button3.buttonClock.getTime())
                    elif len(button3.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button3.timesOff[-1] = button3.buttonClock.getTime()
                    if not button3.wasClicked:
                        # end routine when button3 is clicked
                        continueRoutine = False
                    if not button3.wasClicked:
                        # run callback code when button3 is clicked
                        pass
            # take note of whether button3 was clicked, so that next frame we know if clicks are new
            button3.wasClicked = button3.isClicked and button3.status == STARTED
            # *button4* updates
            
            # if button4 is starting this frame...
            if button4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button4.frameNStart = frameN  # exact frame index
                button4.tStart = t  # local t and not account for scr refresh
                button4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button4, 'tStartRefresh')  # time at next scr refresh
                # update status
                button4.status = STARTED
                button4.setAutoDraw(True)
            
            # if button4 is active this frame...
            if button4.status == STARTED:
                # update params
                pass
                # check whether button4 has been pressed
                if button4.isClicked:
                    if not button4.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button4.timesOn.append(button4.buttonClock.getTime())
                        button4.timesOff.append(button4.buttonClock.getTime())
                    elif len(button4.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button4.timesOff[-1] = button4.buttonClock.getTime()
                    if not button4.wasClicked:
                        # end routine when button4 is clicked
                        continueRoutine = False
                    if not button4.wasClicked:
                        # run callback code when button4 is clicked
                        pass
            # take note of whether button4 was clicked, so that next frame we know if clicks are new
            button4.wasClicked = button4.isClicked and button4.status == STARTED
            # *button5* updates
            
            # if button5 is starting this frame...
            if button5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button5.frameNStart = frameN  # exact frame index
                button5.tStart = t  # local t and not account for scr refresh
                button5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button5, 'tStartRefresh')  # time at next scr refresh
                # update status
                button5.status = STARTED
                button5.setAutoDraw(True)
            
            # if button5 is active this frame...
            if button5.status == STARTED:
                # update params
                pass
                # check whether button5 has been pressed
                if button5.isClicked:
                    if not button5.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button5.timesOn.append(button5.buttonClock.getTime())
                        button5.timesOff.append(button5.buttonClock.getTime())
                    elif len(button5.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button5.timesOff[-1] = button5.buttonClock.getTime()
                    if not button5.wasClicked:
                        # end routine when button5 is clicked
                        continueRoutine = False
                    if not button5.wasClicked:
                        # run callback code when button5 is clicked
                        pass
            # take note of whether button5 was clicked, so that next frame we know if clicks are new
            button5.wasClicked = button5.isClicked and button5.status == STARTED
            # *button6* updates
            
            # if button6 is starting this frame...
            if button6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button6.frameNStart = frameN  # exact frame index
                button6.tStart = t  # local t and not account for scr refresh
                button6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button6, 'tStartRefresh')  # time at next scr refresh
                # update status
                button6.status = STARTED
                button6.setAutoDraw(True)
            
            # if button6 is active this frame...
            if button6.status == STARTED:
                # update params
                pass
                # check whether button6 has been pressed
                if button6.isClicked:
                    if not button6.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button6.timesOn.append(button6.buttonClock.getTime())
                        button6.timesOff.append(button6.buttonClock.getTime())
                    elif len(button6.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button6.timesOff[-1] = button6.buttonClock.getTime()
                    if not button6.wasClicked:
                        # end routine when button6 is clicked
                        continueRoutine = False
                    if not button6.wasClicked:
                        # run callback code when button6 is clicked
                        pass
            # take note of whether button6 was clicked, so that next frame we know if clicks are new
            button6.wasClicked = button6.isClicked and button6.status == STARTED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ResponseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Response" ---
        for thisComponent in ResponseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Response.stopped', globalClock.getTime())
        # store data for practice (TrialHandler)
        practice.addData('mouse.x', mouse.x)
        practice.addData('mouse.y', mouse.y)
        practice.addData('mouse.leftButton', mouse.leftButton)
        practice.addData('mouse.midButton', mouse.midButton)
        practice.addData('mouse.rightButton', mouse.rightButton)
        practice.addData('mouse.time', mouse.time)
        practice.addData('mouse.clicked_name', mouse.clicked_name)
        practice.addData('button1.numClicks', button1.numClicks)
        if button1.numClicks:
           practice.addData('button1.timesOn', button1.timesOn)
           practice.addData('button1.timesOff', button1.timesOff)
        else:
           practice.addData('button1.timesOn', "")
           practice.addData('button1.timesOff', "")
        practice.addData('button2.numClicks', button2.numClicks)
        if button2.numClicks:
           practice.addData('button2.timesOn', button2.timesOn)
           practice.addData('button2.timesOff', button2.timesOff)
        else:
           practice.addData('button2.timesOn', "")
           practice.addData('button2.timesOff', "")
        practice.addData('button3.numClicks', button3.numClicks)
        if button3.numClicks:
           practice.addData('button3.timesOn', button3.timesOn)
           practice.addData('button3.timesOff', button3.timesOff)
        else:
           practice.addData('button3.timesOn', "")
           practice.addData('button3.timesOff', "")
        practice.addData('button4.numClicks', button4.numClicks)
        if button4.numClicks:
           practice.addData('button4.timesOn', button4.timesOn)
           practice.addData('button4.timesOff', button4.timesOff)
        else:
           practice.addData('button4.timesOn', "")
           practice.addData('button4.timesOff', "")
        practice.addData('button5.numClicks', button5.numClicks)
        if button5.numClicks:
           practice.addData('button5.timesOn', button5.timesOn)
           practice.addData('button5.timesOff', button5.timesOff)
        else:
           practice.addData('button5.timesOn', "")
           practice.addData('button5.timesOff', "")
        practice.addData('button6.numClicks', button6.numClicks)
        if button6.numClicks:
           practice.addData('button6.timesOn', button6.timesOn)
           practice.addData('button6.timesOff', button6.timesOff)
        else:
           practice.addData('button6.timesOn', "")
           practice.addData('button6.timesOff', "")
        # Run 'End Routine' code from code_3
        # Get the list of button presses (True/False for each button)
        button_responses = [button1.isClicked, button2.isClicked, button3.isClicked, button4.isClicked, button5.isClicked, button6.isClicked]
        
        # Find the index of the pressed button
        if any(button_responses):  # Check if any button was pressed
            response_index = button_responses.index(True)  # Get the index of the pressed button
            selected_emotion = shuffled_emotions[response_index]  # Map to the corresponding emotion
            thisExp.addData("Selected_Emotion", selected_emotion)  # Log the response
        else:
            selected_emotion = "No Response"  # Handle case where no button was pressed
            thisExp.addData("Selected_Emotion", selected_emotion)
        
        # the Routine "Response" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'practice'
    
    
    # --- Prepare to start Routine "Instructions2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instructions2.started', globalClock.getTime())
    text_5.setText('The practice trials are now complete. The real task trials will now begin.\n\nWhen you are ready, press any key to continue. The first trial will begin immediately.')
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    Instructions2Components = [text_5, key_resp_3]
    for thisComponent in Instructions2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        
        # if text_5 is starting this frame...
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_5.status = STARTED
            text_5.setAutoDraw(True)
        
        # if text_5 is active this frame...
        if text_5.status == STARTED:
            # update params
            pass
        
        # *key_resp_3* updates
        waitOnFlip = False
        
        # if key_resp_3 is starting this frame...
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions2" ---
    for thisComponent in Instructions2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instructions2.stopped', globalClock.getTime())
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    thisExp.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        thisExp.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.addData('key_resp_3.duration', key_resp_3.duration)
    thisExp.nextEntry()
    # the Routine "Instructions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('EmotionFace_Stimuli.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "fixationcross" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('fixationcross.started', globalClock.getTime())
        # keep track of which components have finished
        fixationcrossComponents = [text_7]
        for thisComponent in fixationcrossComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixationcross" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_7* updates
            
            # if text_7 is starting this frame...
            if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_7.frameNStart = frameN  # exact frame index
                text_7.tStart = t  # local t and not account for scr refresh
                text_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_7.status = STARTED
                text_7.setAutoDraw(True)
            
            # if text_7 is active this frame...
            if text_7.status == STARTED:
                # update params
                pass
            
            # if text_7 is stopping this frame...
            if text_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_7.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_7.tStop = t  # not accounting for scr refresh
                    text_7.frameNStop = frameN  # exact frame index
                    # update status
                    text_7.status = FINISHED
                    text_7.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationcrossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixationcross" ---
        for thisComponent in fixationcrossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('fixationcross.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "FaceStimuli" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('FaceStimuli.started', globalClock.getTime())
        FaceStimuli1.setImage(EmotionFace_Stimuli)
        # keep track of which components have finished
        FaceStimuliComponents = [FaceStimuli1]
        for thisComponent in FaceStimuliComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "FaceStimuli" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.3:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FaceStimuli1* updates
            
            # if FaceStimuli1 is starting this frame...
            if FaceStimuli1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FaceStimuli1.frameNStart = frameN  # exact frame index
                FaceStimuli1.tStart = t  # local t and not account for scr refresh
                FaceStimuli1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FaceStimuli1, 'tStartRefresh')  # time at next scr refresh
                # update status
                FaceStimuli1.status = STARTED
                FaceStimuli1.setAutoDraw(True)
            
            # if FaceStimuli1 is active this frame...
            if FaceStimuli1.status == STARTED:
                # update params
                pass
            
            # if FaceStimuli1 is stopping this frame...
            if FaceStimuli1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FaceStimuli1.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    FaceStimuli1.tStop = t  # not accounting for scr refresh
                    FaceStimuli1.frameNStop = frameN  # exact frame index
                    # update status
                    FaceStimuli1.status = FINISHED
                    FaceStimuli1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FaceStimuliComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "FaceStimuli" ---
        for thisComponent in FaceStimuliComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('FaceStimuli.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.300000)
        
        # --- Prepare to start Routine "Blank" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Blank.started', globalClock.getTime())
        # keep track of which components have finished
        BlankComponents = []
        for thisComponent in BlankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Blank" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > 0.5-frameTolerance:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BlankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Blank" ---
        for thisComponent in BlankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Blank.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "Response" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Response.started', globalClock.getTime())
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        button1.setText(button1.text)
        # reset button1 to account for continued clicks & clear times on/off
        button1.reset()
        button2.setText(button2.text)
        # reset button2 to account for continued clicks & clear times on/off
        button2.reset()
        button3.setText(button3.text)
        # reset button3 to account for continued clicks & clear times on/off
        button3.reset()
        button4.setText(button4.text)
        # reset button4 to account for continued clicks & clear times on/off
        button4.reset()
        button5.setText(button5.text)
        # reset button5 to account for continued clicks & clear times on/off
        button5.reset()
        button6.setText(button6.text)
        # reset button6 to account for continued clicks & clear times on/off
        button6.reset()
        # Run 'Begin Routine' code from code_3
        # Define the original list of emotions
        emotions = ["Happy", "Sad", "Surprised", "Angry", "Scared", "Disgusted"]
        
        # Randomize the order
        shuffled_emotions = emotions.copy()
        shuffle(shuffled_emotions)
        
        # Assign the randomized labels to the buttons
        button1.text = shuffled_emotions[0]
        button2.text = shuffled_emotions[1]
        button3.text = shuffled_emotions[2]
        button4.text = shuffled_emotions[3]
        button5.text = shuffled_emotions[4]
        button6.text = shuffled_emotions[5]
        
        # keep track of which components have finished
        ResponseComponents = [text_6, mouse, button1, button2, button3, button4, button5, button6]
        for thisComponent in ResponseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Response" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_6* updates
            
            # if text_6 is starting this frame...
            if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_6.status = STARTED
                text_6.setAutoDraw(True)
            
            # if text_6 is active this frame...
            if text_6.status == STARTED:
                # update params
                pass
            # *mouse* updates
            
            # if mouse is starting this frame...
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames(['button1', 'button2', 'button3', 'button4', 'button5', 'button6'], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            # *button1* updates
            
            # if button1 is starting this frame...
            if button1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button1.frameNStart = frameN  # exact frame index
                button1.tStart = t  # local t and not account for scr refresh
                button1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button1, 'tStartRefresh')  # time at next scr refresh
                # update status
                button1.status = STARTED
                button1.setAutoDraw(True)
            
            # if button1 is active this frame...
            if button1.status == STARTED:
                # update params
                pass
                # check whether button1 has been pressed
                if button1.isClicked:
                    if not button1.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button1.timesOn.append(button1.buttonClock.getTime())
                        button1.timesOff.append(button1.buttonClock.getTime())
                    elif len(button1.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button1.timesOff[-1] = button1.buttonClock.getTime()
                    if not button1.wasClicked:
                        # end routine when button1 is clicked
                        continueRoutine = False
                    if not button1.wasClicked:
                        # run callback code when button1 is clicked
                        pass
            # take note of whether button1 was clicked, so that next frame we know if clicks are new
            button1.wasClicked = button1.isClicked and button1.status == STARTED
            # *button2* updates
            
            # if button2 is starting this frame...
            if button2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button2.frameNStart = frameN  # exact frame index
                button2.tStart = t  # local t and not account for scr refresh
                button2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button2, 'tStartRefresh')  # time at next scr refresh
                # update status
                button2.status = STARTED
                button2.setAutoDraw(True)
            
            # if button2 is active this frame...
            if button2.status == STARTED:
                # update params
                pass
                # check whether button2 has been pressed
                if button2.isClicked:
                    if not button2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button2.timesOn.append(button2.buttonClock.getTime())
                        button2.timesOff.append(button2.buttonClock.getTime())
                    elif len(button2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button2.timesOff[-1] = button2.buttonClock.getTime()
                    if not button2.wasClicked:
                        # end routine when button2 is clicked
                        continueRoutine = False
                    if not button2.wasClicked:
                        # run callback code when button2 is clicked
                        pass
            # take note of whether button2 was clicked, so that next frame we know if clicks are new
            button2.wasClicked = button2.isClicked and button2.status == STARTED
            # *button3* updates
            
            # if button3 is starting this frame...
            if button3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button3.frameNStart = frameN  # exact frame index
                button3.tStart = t  # local t and not account for scr refresh
                button3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button3, 'tStartRefresh')  # time at next scr refresh
                # update status
                button3.status = STARTED
                button3.setAutoDraw(True)
            
            # if button3 is active this frame...
            if button3.status == STARTED:
                # update params
                pass
                # check whether button3 has been pressed
                if button3.isClicked:
                    if not button3.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button3.timesOn.append(button3.buttonClock.getTime())
                        button3.timesOff.append(button3.buttonClock.getTime())
                    elif len(button3.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button3.timesOff[-1] = button3.buttonClock.getTime()
                    if not button3.wasClicked:
                        # end routine when button3 is clicked
                        continueRoutine = False
                    if not button3.wasClicked:
                        # run callback code when button3 is clicked
                        pass
            # take note of whether button3 was clicked, so that next frame we know if clicks are new
            button3.wasClicked = button3.isClicked and button3.status == STARTED
            # *button4* updates
            
            # if button4 is starting this frame...
            if button4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button4.frameNStart = frameN  # exact frame index
                button4.tStart = t  # local t and not account for scr refresh
                button4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button4, 'tStartRefresh')  # time at next scr refresh
                # update status
                button4.status = STARTED
                button4.setAutoDraw(True)
            
            # if button4 is active this frame...
            if button4.status == STARTED:
                # update params
                pass
                # check whether button4 has been pressed
                if button4.isClicked:
                    if not button4.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button4.timesOn.append(button4.buttonClock.getTime())
                        button4.timesOff.append(button4.buttonClock.getTime())
                    elif len(button4.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button4.timesOff[-1] = button4.buttonClock.getTime()
                    if not button4.wasClicked:
                        # end routine when button4 is clicked
                        continueRoutine = False
                    if not button4.wasClicked:
                        # run callback code when button4 is clicked
                        pass
            # take note of whether button4 was clicked, so that next frame we know if clicks are new
            button4.wasClicked = button4.isClicked and button4.status == STARTED
            # *button5* updates
            
            # if button5 is starting this frame...
            if button5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button5.frameNStart = frameN  # exact frame index
                button5.tStart = t  # local t and not account for scr refresh
                button5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button5, 'tStartRefresh')  # time at next scr refresh
                # update status
                button5.status = STARTED
                button5.setAutoDraw(True)
            
            # if button5 is active this frame...
            if button5.status == STARTED:
                # update params
                pass
                # check whether button5 has been pressed
                if button5.isClicked:
                    if not button5.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button5.timesOn.append(button5.buttonClock.getTime())
                        button5.timesOff.append(button5.buttonClock.getTime())
                    elif len(button5.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button5.timesOff[-1] = button5.buttonClock.getTime()
                    if not button5.wasClicked:
                        # end routine when button5 is clicked
                        continueRoutine = False
                    if not button5.wasClicked:
                        # run callback code when button5 is clicked
                        pass
            # take note of whether button5 was clicked, so that next frame we know if clicks are new
            button5.wasClicked = button5.isClicked and button5.status == STARTED
            # *button6* updates
            
            # if button6 is starting this frame...
            if button6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button6.frameNStart = frameN  # exact frame index
                button6.tStart = t  # local t and not account for scr refresh
                button6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button6, 'tStartRefresh')  # time at next scr refresh
                # update status
                button6.status = STARTED
                button6.setAutoDraw(True)
            
            # if button6 is active this frame...
            if button6.status == STARTED:
                # update params
                pass
                # check whether button6 has been pressed
                if button6.isClicked:
                    if not button6.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button6.timesOn.append(button6.buttonClock.getTime())
                        button6.timesOff.append(button6.buttonClock.getTime())
                    elif len(button6.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button6.timesOff[-1] = button6.buttonClock.getTime()
                    if not button6.wasClicked:
                        # end routine when button6 is clicked
                        continueRoutine = False
                    if not button6.wasClicked:
                        # run callback code when button6 is clicked
                        pass
            # take note of whether button6 was clicked, so that next frame we know if clicks are new
            button6.wasClicked = button6.isClicked and button6.status == STARTED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ResponseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Response" ---
        for thisComponent in ResponseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Response.stopped', globalClock.getTime())
        # store data for trials (TrialHandler)
        trials.addData('mouse.x', mouse.x)
        trials.addData('mouse.y', mouse.y)
        trials.addData('mouse.leftButton', mouse.leftButton)
        trials.addData('mouse.midButton', mouse.midButton)
        trials.addData('mouse.rightButton', mouse.rightButton)
        trials.addData('mouse.time', mouse.time)
        trials.addData('mouse.clicked_name', mouse.clicked_name)
        trials.addData('button1.numClicks', button1.numClicks)
        if button1.numClicks:
           trials.addData('button1.timesOn', button1.timesOn)
           trials.addData('button1.timesOff', button1.timesOff)
        else:
           trials.addData('button1.timesOn', "")
           trials.addData('button1.timesOff', "")
        trials.addData('button2.numClicks', button2.numClicks)
        if button2.numClicks:
           trials.addData('button2.timesOn', button2.timesOn)
           trials.addData('button2.timesOff', button2.timesOff)
        else:
           trials.addData('button2.timesOn', "")
           trials.addData('button2.timesOff', "")
        trials.addData('button3.numClicks', button3.numClicks)
        if button3.numClicks:
           trials.addData('button3.timesOn', button3.timesOn)
           trials.addData('button3.timesOff', button3.timesOff)
        else:
           trials.addData('button3.timesOn', "")
           trials.addData('button3.timesOff', "")
        trials.addData('button4.numClicks', button4.numClicks)
        if button4.numClicks:
           trials.addData('button4.timesOn', button4.timesOn)
           trials.addData('button4.timesOff', button4.timesOff)
        else:
           trials.addData('button4.timesOn', "")
           trials.addData('button4.timesOff', "")
        trials.addData('button5.numClicks', button5.numClicks)
        if button5.numClicks:
           trials.addData('button5.timesOn', button5.timesOn)
           trials.addData('button5.timesOff', button5.timesOff)
        else:
           trials.addData('button5.timesOn', "")
           trials.addData('button5.timesOff', "")
        trials.addData('button6.numClicks', button6.numClicks)
        if button6.numClicks:
           trials.addData('button6.timesOn', button6.timesOn)
           trials.addData('button6.timesOff', button6.timesOff)
        else:
           trials.addData('button6.timesOn', "")
           trials.addData('button6.timesOff', "")
        # Run 'End Routine' code from code_3
        # Get the list of button presses (True/False for each button)
        button_responses = [button1.isClicked, button2.isClicked, button3.isClicked, button4.isClicked, button5.isClicked, button6.isClicked]
        
        # Find the index of the pressed button
        if any(button_responses):  # Check if any button was pressed
            response_index = button_responses.index(True)  # Get the index of the pressed button
            selected_emotion = shuffled_emotions[response_index]  # Map to the corresponding emotion
            thisExp.addData("Selected_Emotion", selected_emotion)  # Log the response
        else:
            selected_emotion = "No Response"  # Handle case where no button was pressed
            thisExp.addData("Selected_Emotion", selected_emotion)
        
        # the Routine "Response" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "EndMessage" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('EndMessage.started', globalClock.getTime())
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    EndMessageComponents = [text_4, key_resp_2]
    for thisComponent in EndMessageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EndMessage" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndMessageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EndMessage" ---
    for thisComponent in EndMessageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('EndMessage.stopped', globalClock.getTime())
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "EndMessage" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
