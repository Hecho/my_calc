import numpy as np
import wx
import math

class FrustrumCalculatorPanel(wx.Panel):
    def __init__(self, parent):
        super(FrustrumCalculatorPanel, self).__init__(parent)

        self.label1 = wx.StaticText(self, label="Enter base width:")
        self.entry1 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        
        self.label2 = wx.StaticText(self, label="Enter base depth:")
        self.entry2 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)

        self.label3 = wx.StaticText(self, label="Enter length:")
        self.entry3 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)

        self.label4 = wx.StaticText(self, label="Enter top width:")
        self.entry4 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)

        self.label5 = wx.StaticText(self, label="Enter top depth:")
        self.entry5 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)

        self.calculate_button = wx.Button(self, label="Calculate")
        self.calculate_button.Bind(wx.EVT_BUTTON, self.calculate)

        # Bind the Enter key in entry1 to move focus to entry2
        self.entry1.Bind(wx.EVT_TEXT_ENTER, lambda event: self.entry2.SetFocus())

        # Bind the Enter key in entry2 to move focus to entry3
        self.entry2.Bind(wx.EVT_TEXT_ENTER, lambda event: self.entry3.SetFocus())

        # Bind the Enter key in entry3 to move focus to entry4
        self.entry3.Bind(wx.EVT_TEXT_ENTER, lambda event: self.entry4.SetFocus())

        # Bind the Enter key in entry4 to move focus to entry5
        self.entry4.Bind(wx.EVT_TEXT_ENTER, lambda event: self.entry5.SetFocus())

        # Bind the Enter key press in the last TextCtrl to the calculate method
        self.entry5.Bind(wx.EVT_TEXT_ENTER, self.calculate)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.label1, 0, wx.ALL, 5)
        self.sizer.Add(self.entry1, 0, wx.EXPAND|wx.ALL, 5)
        self.sizer.Add(self.label2, 0, wx.ALL, 5)
        self.sizer.Add(self.entry2, 0, wx.EXPAND|wx.ALL, 5)
        self.sizer.Add(self.label3, 0, wx.ALL, 5)  # Adding label3 to the sizer
        self.sizer.Add(self.entry3, 0, wx.EXPAND|wx.ALL, 5)  # Adding entry3 to the sizer
        self.sizer.Add(self.label4, 0, wx.ALL, 5)
        self.sizer.Add(self.entry4, 0, wx.EXPAND|wx.ALL, 5)
        self.sizer.Add(self.label5, 0, wx.ALL, 5)
        self.sizer.Add(self.entry5, 0, wx.EXPAND|wx.ALL, 5)
        self.sizer.Add(self.calculate_button, 0, wx.ALL, 5)
        
        self.SetSizer(self.sizer)
        self.Layout()
    
    def calculate(self, event):
        try:
            bw = float(self.entry1.GetValue())
            bd = float(self.entry2.GetValue())
            h = float(self.entry3.GetValue())
            tw = float(self.entry4.GetValue())
            td = float(self.entry5.GetValue())

            # Calculate coordinates for the planes
            A, B, C, D = find_coords(bw, bd, h, tw, td)

            normal_vector1 = calculate_normal_vector(A, B, C)
            normal_vector2 = calculate_normal_vector(A, C, D)
            
            angle = calculate_angle_between_vectors(normal_vector1, normal_vector2)
            
            # Convert the angle to string before passing it to wx.MessageBox
            wx.MessageBox(f"The angle between the normal vectors is: {str(angle)} degrees", "Result", wx.OK | wx.ICON_INFORMATION)
            
        except ValueError:
            wx.MessageBox("Invalid input. Please enter valid numbers.", "Error", wx.OK | wx.ICON_ERROR)
            
def find_coords(bw,bd,h,tw,td):
    # A always equals (0,0,0)
    A = (0,0,0)
    # find B
    B = (-bw , 0, 0)
    # find C
    C = (-(bw - tw) / 2, (bd - td) / 2, h)
    # find D
    D = (0, bd, h)

    return A, B, C, D

def calculate_normal_vector(A, B, C):
    # Create vectors AB and AC
    AB = np.subtract(B, A)
    AC = np.subtract(C, A)

    # Calculate the cross product of AB and AC
    normal_vector = np.cross(AB, AC)

    # Normalize the normal vector
    normal_vector = normal_vector / np.linalg.norm(normal_vector)

    return normal_vector

# Test the function
#bw, bd, h, tw, td = 600, 600, 100, 282, 282
#normal_vector1, normal_vector2 = calculate_normal_vectors(bw, bd, h, tw, td)
#print("Normal vector of the first plane: ", normal_vector1)
#print("Normal vector of the second plane: ", normal_vector2)

def calculate_angle_between_vectors(v1, v2):
    # Calculate the dot product
    dot_product = np.dot(v1, v2)

    # Calculate the magnitudes of the vectors
    magnitude_v1 = np.linalg.norm(v1)
    magnitude_v2 = np.linalg.norm(v2)

    # Calculate the cosine of the angle
    cos_angle = dot_product / (magnitude_v1 * magnitude_v2)

    # Calculate the angle in radians
    angle_rad = np.arccos(cos_angle)

    # Convert the angle to degrees
    angle_deg = np.degrees(angle_rad)

    return angle_deg

# Test the function


    