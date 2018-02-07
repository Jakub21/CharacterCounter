'''
GUI Character Counter
Feb. 2018
'''

import wx

class mainFrame(wx.Frame):
    def __init__(self):
        super(mainFrame, self).__init__(None, title='Character Counter')

        self.initUI()
        self.Show()

    def initUI(self):
        '''Create main Panel'''
        self.panel = wx.Panel(self)
        self.sizer = wx.GridBagSizer()


        btt = wx.Button(self.panel, label='Load')
        self.sizer.Add(btt, pos=(0,0))
        btt.Bind(wx.EVT_BUTTON, self.actionSelectFile)

        btt = wx.Button(self.panel, label='Calculate')
        self.sizer.Add(btt, pos=(1,0))
        btt.Bind(wx.EVT_BUTTON, self.actionCountChars)

        btt = wx.Button(self.panel, label='Show Plot')
        self.sizer.Add(btt, pos=(2,0))
        btt.Bind(wx.EVT_BUTTON, self.actionShowPlot)

        btt = wx.Button(self.panel, label='Quit')
        self.sizer.Add(btt, pos=(3,0))
        btt.Bind(wx.EVT_BUTTON, self.actionQuit)


        #self.sizer.AddGrowableRow()
        #self.sizer.AddGrowableCol()
        self.panel.SetSizerAndFit(self.sizer)

    def action(self, event):
        print('actionDEFAULT')

    def actionSelectFile(self, event):
        '''Open "select file" dialog'''
        print('actionSelectFile')

    def actionCountChars(self, event):
        print('actionCountChars')

    def actionShowPlot(self, event):
        print('actionShowPlot')

    def actionQuit(self, event):
        self.Close()


if __name__ == '__main__':
    app = wx.App()
    frame = mainFrame()
    app.MainLoop()
