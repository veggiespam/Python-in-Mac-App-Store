import wx

def main():
    app = wx.PySimpleApp()
    colors = ['Red', 'Blue', 'Green', 'Pink', 'White']
    dialog = wx.SingleChoiceDialog(
        None, 'Pick something...', 'Pick a Color', colors)
    dialog.ShowModal()
