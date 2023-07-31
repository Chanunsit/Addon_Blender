import bpy
import webbrowser
from bpy.types import ( PropertyGroup, )
from bpy.props import (PointerProperty, StringProperty)

class MyProperties(PropertyGroup):
    saveList : StringProperty(name="Save List")

class OpenWebsiteOperator(bpy.types.Operator):
    bl_idname = "addon.open_website"
    bl_label = "Open Website"
    bl_options = {'REGISTER'}
    action : StringProperty(name="action")

    def execute(self, context):
        

        if self.action == "@_JiraDashBoard":
            self.Go_JiraDashBoard(self, context)
        elif self.action == "@_WorkLogPro":
            self.Go_WorkLogPro(self, context)
        elif self.action == "@_BackOffice":
            self.Go_BackOffice(self, context)

        return {'FINISHED'}
    
    @staticmethod
    def Go_JiraDashBoard(self, context):
        website_url = "https://jira.bistudio.com/secure/Dashboard.jspa"  
        webbrowser.open(website_url)
        print("Go Jira DashBoard")
        return {'FINISHED'}
    @staticmethod
    def Go_WorkLogPro(self, context):
        website_url = "https://jira.bistudio.com/secure/WPShowTimesheetAction!customTimesheet.jspa?periodMode=MONTH&targetType=USER&calendarType=CUSTOM&groupingType=ISSUE#targetType=USER&targetKey=mantanakulnat&groupingType=Issue&periodMode=MONTH&startDate=2023-07-01&endDate=2023-07-31&&&periodLocked=false&calendarType=CUSTOM&saveToUserHistory=false&extraIssueFilter=&showIssuesWithoutWorklog=false&viewType=TIMESHEET" 
        webbrowser.open(website_url)
        print("Go WorkLogPro")
        return {'FINISHED'}
    @staticmethod
    def Go_BackOffice(self, context):
        website_url = "https://backoffice.bistudio.com/" 
        webbrowser.open(website_url)
        print("Go BackOffice")
        return {'FINISHED'}
classes = [MyProperties,OpenWebsiteOperator]
def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
