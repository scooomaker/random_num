import wx
import random

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Random Number Generator')

        # create menu bar
        self.menu_bar = wx.MenuBar()
        self.SetMenuBar(self.menu_bar)

        # create file menu
        self.file_menu = wx.Menu()
        self.menu_bar.Append(self.file_menu, '&File')
        self.Bind(wx.EVT_MENU, self.on_exit, self.file_menu.Append(wx.ID_EXIT, 'E&xit\tCtrl+W'))

        # create mode menu
        self.mode_menu = wx.Menu()
        self.menu_bar.Append(self.mode_menu, '&Mode')
        self.Bind(wx.EVT_MENU, self.on_mode_1, self.mode_menu.Append(wx.ID_ANY, '&Mode 1\tCtrl+1'))
        self.Bind(wx.EVT_MENU, self.on_mode_2, self.mode_menu.Append(wx.ID_ANY, '&Mode 2\tCtrl+2'))
        self.Bind(wx.EVT_MENU, self.on_mode_3, self.mode_menu.Append(wx.ID_ANY, '&Mode 3\tCtrl+3'))

        # create main panel
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel.SetSizer(self.sizer)

        # create mode 1 panel
        self.mode_1_panel = wx.Panel(self.panel)
        self.mode_1_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.mode_1_panel.SetSizer(self.mode_1_sizer)
        self.mode_1_button = wx.Button(self.mode_1_panel, label='Generate')
        self.mode_1_sizer.Add(self.mode_1_button, 0, wx.ALL, 5)
        self.mode_1_text = wx.StaticText(self.mode_1_panel, label='', style=wx.ALIGN_CENTER)
        self.mode_1_sizer.Add(self.mode_1_text, 0, wx.ALL, 5)
        self.Bind(wx.EVT_BUTTON, self.on_mode_1_button, self.mode_1_button)
        self.sizer.Add(self.mode_1_panel, 0, wx.EXPAND)
        self.mode_1_panel.Hide()

        # create mode 2 panel
        self.mode_2_panel = wx.Panel(self.panel)
        self.mode_2_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.mode_2_panel.SetSizer(self.mode_2_sizer)
        self.mode_2_button = wx.Button(self.mode_2_panel, label='Generate')
        self.mode_2_sizer.Add(self.mode_2_button, 0, wx.ALL, 5)
        self.mode_2_text = wx.StaticText(self.mode_2_panel, label='', style=wx.ALIGN_CENTER)
        self.mode_2_sizer.Add(self.mode_2_text, 0, wx.ALL, 5)
        self.Bind(wx.EVT_BUTTON, self.on_mode_2_button, self.mode_2_button)
        self.sizer.Add(self.mode_2_panel, 0, wx.EXPAND)
        self.mode_2_panel.Hide()


         # create mode 3 panel
        self.mode_3_panel = wx.Panel(self.panel)
        self.mode_3_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.mode_3_panel.SetSizer(self.mode_3_sizer)
        self.mode_3_text_1 = wx.StaticText(self.mode_3_panel, label='Enter range:')
        self.mode_3_sizer.Add(self.mode_3_text_1, 0, wx.ALL, 5)
        self.mode_3_text_ctrl_1 = wx.TextCtrl(self.mode_3_panel)
        self.mode_3_sizer.Add(self.mode_3_text_ctrl_1, 0, wx.ALL, 5)
        self.mode_3_text_2 = wx.StaticText(self.mode_3_panel, label='to')
        self.mode_3_sizer.Add(self.mode_3_text_2, 0, wx.ALL, 5)
        self.mode_3_text_ctrl_2 = wx.TextCtrl(self.mode_3_panel)
        self.mode_3_sizer.Add(self.mode_3_text_ctrl_2, 0, wx.ALL, 5)
        self.mode_3_button = wx.Button(self.mode_3_panel, label='Generate')
        self.mode_3_sizer.Add(self.mode_3_button, 0, wx.ALL, 5)
        self.mode_3_text = wx.StaticText(self.mode_3_panel, label='', style=wx.ALIGN_CENTER)
        self.mode_3_sizer.Add(self.mode_3_text, 0, wx.ALL, 5)
        self.Bind(wx.EVT_BUTTON, self.on_mode_3_button, self.mode_3_button)
        self.sizer.Add(self.mode_3_panel, 0, wx.EXPAND)
        self.mode_3_panel.Hide()

        self.Show()

    def on_exit(self, event):
        self.Close()

    def on_mode_1(self, event):
        self.mode_1_panel.Show()
        self.mode_2_panel.Hide()
        self.mode_3_panel.Hide()
        self.sizer.Layout()

    def on_mode_2(self, event):
        self.mode_1_panel.Hide()
        self.mode_2_panel.Show()
        self.mode_3_panel.Hide()
        self.sizer.Layout()

    def on_mode_3(self, event):
        self.mode_1_panel.Hide()
        self.mode_2_panel.Hide()
        self.mode_3_panel.Show()
        self.sizer.Layout()

    def on_mode_1_button(self, event):
        self.mode_1_text.SetLabel(str(random.randint(1, 26)))

    def on_mode_2_button(self, event):
        nums = []
        while len(nums) < 5:
            num = random.randint(1, 26)
            if num not in nums:
                nums.append(num)
        self.mode_2_text.SetLabel(', '.join(str(num) for num in nums))

    def on_mode_3_button(self, event):
        try:
            num_1 = int(self.mode_3_text_ctrl_1.GetValue())
            num_2 = int(self.mode_3_text_ctrl_2.GetValue())
            if num_1 > num_2:
                num_1, num_2 = num_2, num_1
            self.mode_3_text.SetLabel(str(random.randint(num_1, num_2)))
        except ValueError:
            self.mode_3_text.SetLabel('Invalid input')

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()
