import numpy as np
import wx
import math

class FrustrumCalculatorPanel(wx.Panel):
    def __init__(self, parent):
        super(FrustrumCalculatorPanel, self).__init__(parent)

        labels = ["Enter base width:", "Enter base depth:", "Enter length:", "Enter top width:", "Enter top depth:"]
        self.entries = [wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER) for _ in labels]

        # Bind the Enter key in each entry to move focus to the next entry
        for i in range(len(self.entries) - 1):
            self.entries[i].Bind(wx.EVT_TEXT_ENTER, lambda event: self.entries[i + 1].SetFocus())

        # Bind the Enter key press in the last TextCtrl to the calculate method
        self.entries[-1].Bind(wx.EVT_TEXT_ENTER, self.calculate)

        self.calculate_button = wx.Button(self, label="Calculate")
        self.calculate_button.Bind(wx.EVT_BUTTON, self.calculate)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        for label, entry in zip(labels, self.entries):
            self.sizer.Add(wx.StaticText(self, label=label), 0, wx.ALL, 5)
            self.sizer.Add(entry, 0, wx.EXPAND|wx.ALL, 5)
        self.sizer.Add(self.calculate_button, 0, wx.ALL, 5)
        
        self.SetSizer(self.sizer)
        self.Layout()
    
    def calculate(self, event):
        try:
            bw = float(self.entries[0].GetValue())
            bd = float(self.entries[1].GetValue())
            h = float(self.entries[2].GetValue())
            tw = float(self.entries[3].GetValue())
            td = float(self.entries[4].GetValue())

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

    final_angle = 2*(90 - (angle_deg/2))

    return final_angle
