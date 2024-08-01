#coding:utf-8
import sys

import wx                  # This module uses the new wx namespace
import wx.html
import wx.lib.wxpTag

#---------------------------------------------------------------------------

class HtmlWin(wx.html.HtmlWindow):

    def __init__(self, parent, id=-1, size=(420, 300)):

        wx.html.HtmlWindow.__init__(self, parent, id, size=size)
        if "gtk2" in wx.PlatformInfo:
            self.SetStandardFonts()


    def OnLinkClicked(self, link):

        wx.LaunchDefaultBrowser(link.GetHref())

class MyAboutBox(wx.Dialog):
    text = u'''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title></title>
</head>

<body bgcolor="#E8E8E8">
<table  width="100%", cellspacing="0"
cellpadding="0">
<tr>
    <td align="center" bgcolor="#66A0E4">
    <h3>HCGuardian 进程监控管理器 v1.5</h3><br>
    汇萃智能<br>
    </td>
</tr>
</table>

<p>欢迎使用 <b>HCGuardian ！</b></p> <p>它是一个汇萃科技进程监控管理软件，用于监控守护正在运行的进程，</br>
  </p>
<p>当发现监控中进程被意外关闭时可以自动开启。同时也可以启动，结束，重启进程。</p>
<br>
<p>当前版本：1.5 </p>
</body>
</html>
'''
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, -1, u'关于 HCGuardian v1.5',
                           style=wx.DEFAULT_DIALOG_STYLE)
        html = HtmlWin(self)
        html.SetPage(self.text)
        ir = html.GetInternalRepresentation()
        html.SetSize( (ir.GetWidth()+20, ir.GetHeight()+5) )
        self.SetClientSize(html.GetSize())
        self.CentreOnParent(wx.BOTH)


if __name__ == '__main__':
    app = wx.App()
    dlg = MyAboutBox(None)
    dlg.ShowModal()
    dlg.Destroy()
    app.MainLoop()
