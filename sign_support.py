
import os
import subprocess
import sys
import shutil
import tkMessageBox
import accSelect
import accSelect_support
import defs
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

def set_Tk_var():
    global accounts
    accounts = StringVar()


if sys.platform.__contains__('linux'):

    def openFolder(path):
        os.system('xdg-open "' + path + '"')


if sys.platform.__contains__('win') and not sys.platform.__contains__("darwin"):

    def openFolder(path):
        os.system('explorer.exe "' + path + '"')


def delBkup(backup):
    print 'Deleting Folder: ' + defs.getCmaDir() + '/EXTRACTED/' + load + '/' + backup
    shutil.rmtree(defs.getCmaDir() + '/EXTRACTED/' + load + '/' + backup)
    sys.stdout.flush()
    import sign
    sign.close_window(root)
    sign.vp_start_gui()


def sign(backup):
    if backup != '':
        accSelect_support.pushVars(backup, load)
        import sign
        sign.close_window(root)
        accSelect.vp_start_gui()
    sys.stdout.flush()


def expBkup(backup):
    print 'Opening Folder: ' + defs.getCmaDir() + '/EXTRACTED/' + load + '/' + backup
    openFolder(defs.getCmaDir() + '/EXTRACTED/' + load + '/' + backup)
    sys.stdout.flush()


def init(top, gui, *args, **kwargs):
    global root
    global w
    global top_level
    w = gui
    top_level = top
    root = top


def destroy_window():
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import sign
    sign.vp_start_gui()

def loadPSM():
    global load
    load = 'PSM'


def loadPSP():
    global load
    load = 'PGAME'


def loadPSOne():
    global load
    load = 'PSGAME'


def loadPSV():
    global load
    load = 'APP'


def loadSYS():
    global load
    load = 'SYSTEM'


def getLoad():
    return load


def goSign(acc, ld, bkup, resign):
    global am
    global foldParams
    CMA = defs.getCmaDir()
    cmaKey = defs.getStoredKey(acc)
    cmaAID = defs.getAid(acc)
    import sys
    print ld
    if ld != 'SYSTEM':
        if ld == 'PGAME':
            foldParams = ['game', 'license']
            am = 1
        elif ld == 'APP':
            foldParams = ['app',
             'patch',
             'addcont',
             'appmeta',
             'license',
             'savedata']
            am = 5
        elif ld == 'PSGAME':
            foldParams = ['game', 'license']
            am = 1
        elif ld == 'PSM':
            foldParams = ['game',
             'license',
             'patch',
             'savedata']
            am = 4
        if not os.path.exists(CMA + '/' + ld + '/' + cmaAID + '/' + bkup):
            os.makedirs(CMA + '/' + ld + '/' + cmaAID + '/' + bkup)
        while am != -1:
            if not os.path.exists(CMA + '/' + ld + '/' + cmaAID + '/' + bkup + '/' + foldParams[am]):
                if os.path.exists(CMA + '/EXTRACTED/' + ld + '/' + bkup + '/' + foldParams[am]):
                    os.makedirs(CMA + '/' + ld + '/' + cmaAID + '/' + bkup + '/' + foldParams[am])
            am -= 1

        if ld == 'PGAME':
            foldParams = ['game', 'license']
            am = 1
        elif ld == 'APP':
            foldParams = ['app',
             'patch',
             'addcont',
             'appmeta',
             'license',
             'savedata']
            am = 5
        elif ld == 'PSGAME':
            foldParams = ['game', 'license']
            am = 1
        elif ld == 'PSM':
            foldParams = ['game', 'license']
            am = 1
        while am != -1:
            if sys.platform.__contains__('linux') or sys.platform.__contains__('darwin'):
                print 'Executing: ./psvimg-create -m ' + '"' + CMA + '/EXTRACTED/' + ld + '/' + bkup + '/' + foldParams[am] + '.psvmd-dec" -K ' + cmaKey + ' "' + CMA + '/EXTRACTED/' + ld + '/' + bkup + '/' + foldParams[am] + '" "' + CMA + '/' + ld + '/' + cmaAID + '/' + bkup + '/' + foldParams[am] + '"'
                os.system('./psvimg-create -m "' + CMA + '/EXTRACTED/' + ld + '/' + bkup + '/' + foldParams[am] + '.psvmd-dec" -K ' + cmaKey + ' "' + CMA + '/EXTRACTED/' + ld + '/' + bkup + '/' + foldParams[am] + '" "' + CMA + '/' + ld + '/' + cmaAID + '/' + bkup + '/' + foldParams[am] + '"')
                am -= 1
            if sys.platform.__contains__('win') and not sys.platform.__contains__("darwin"):
                print 'Executing: psvimg-create.exe -m ' + '"' + CMA + '/EXTRACTED/' + ld + '/' + bkup + '/' + foldParams[am] + '.psvmd-dec" -K ' + cmaKey + ' "' + CMA + '/EXTRACTED/' + ld + '/' + bkup + '/' + foldParams[am] + '" "' + CMA + '/' + ld + '/' + cmaAID + '/' + bkup + '/' + foldParams[am] + '"'
                os.system('psvimg-create.exe -m ' + '"' + CMA + '/EXTRACTED/' + ld + '/' + bkup + '/' + foldParams[am] + '.psvmd-dec" -K ' + cmaKey + ' "' + CMA + '/EXTRACTED/' + ld + '/' + bkup + '/' + foldParams[am] + '" "' + CMA + '/' + ld + '/' + cmaAID + '/' + bkup + '/' + foldParams[am] + '"')
                am -= 1

        if not os.path.exists(CMA + '/' + ld + '/' + cmaAID + '/' + bkup + '/sce_sys'):
            print 'Copying Folder: ' + CMA + '/EXTRACTED/' + ld + '/' + bkup + '/sce_sys To: ' + CMA + '/' + ld + '/' + cmaAID + '/' + bkup + '/sce_sys'
            shutil.copytree(CMA + '/EXTRACTED/' + ld + '/' + bkup + '/sce_sys', CMA + '/' + ld + '/' + cmaAID + '/' + bkup + '/sce_sys')
    elif ld == 'SYSTEM':
        if sys.platform.__contains__('linux') or sys.platform.__contains__('darwin'):
            print 'Executing: ./psvimg-create -m ' + '"' + CMA + '/EXTRACTED/' + ld + '/' + bkup + '.psvmd-dec" -K ' + cmaKey + ' "' + CMA + '/EXTRACTED/' + ld + '/' + bkup + '" "' + CMA + '/' + ld + '/' + cmaAID + '/' + bkup + '"'
            os.system('./psvimg-create -m "' + CMA + '/EXTRACTED/' + ld + '/' + bkup + '.psvmd-dec" -K ' + cmaKey + ' "' + CMA + '/EXTRACTED/' + ld + '/' + bkup + '" "' + CMA + '/' + ld + '/' + cmaAID + '/' + bkup + '"')
        if sys.platform.__contains__('win') and not sys.platform.__contains__("darwin"):
            print 'Executing: psvimg-create.exe -m ' + '"' + CMA + '/EXTRACTED/' + ld + '/' + bkup + '.psvmd-dec" -K ' + cmaKey + ' "' + CMA + '/EXTRACTED/' + ld + '/' + bkup + '" "' + CMA + '/' + ld + '/' + cmaAID + '/' + bkup + '"'
            os.system('psvimg-create.exe -m ' + '"' + CMA + '/EXTRACTED/' + ld + '/' + bkup + '.psvmd-dec" -K ' + cmaKey + ' "' + CMA + '/EXTRACTED/' + ld + '/' + bkup + '" "' + CMA + '/' + ld + '/' + cmaAID + '/' + bkup + '"')
        print 'Copying File: ' + CMA + '/EXTRACTED/' + ld + '/' + bkup + '.psvinf To: ' + CMA + '/' + ld + '/' + cmaAID + '/' + bkup + '/' + bkup + '.psvinf'
        shutil.copy(CMA + '/EXTRACTED/' + ld + '/' + bkup + '.psvinf', CMA + '/' + ld + '/' + cmaAID + '/' + bkup + '/' + bkup + '.psvinf')
    if resign == False:
        tkMessageBox.showinfo(title='Pack', message='Packing Complete! (Refresh QCMA!)')
        import sign
        sign.vp_start_gui()

