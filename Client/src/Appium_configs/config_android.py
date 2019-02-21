"""
Andriod strategy vaiables for
Accessibility ID, Class name, ID, Name, XPath, Image
"""
PORT = "4723"
IP = "localhost"
url = "http://"+IP+":"+str(PORT)+"/wd/hub"

android_id = "android:id"
android_widget = "android.widget"
android_view = "android.view"
android = {
    'TextView': android_widget+".TextView",
    'Button': android_widget+".Button",
    'alertTitle': android_id+"/alertTitle",
    'aerr_close': android_id+"/aerr_close",
    'CheckedTextView': android_widget+".CheckedTextView",
    'ViewGroup': android_view+".ViewGroup"
}

gmid_id = "com.mavenir.gmid:id"
UCC_id_login = {
    'dev_settings_fragment': gmid_id+"/dev_settings_fragment",
    'input_login': gmid_id+"/et_input_login",
    'input_password': gmid_id+"/et_input_password",
    'btn_login': gmid_id+"/btn_login",
    'line_name_view': gmid_id+"/line_name_view",
    'parent_layout': gmid_id+"/parent_layout",
    'navigate_button': gmid_id+"/navigate_button",
    'user_status': gmid_id+"/iv_user_status"
}

UCC_id_call = {
    'btn_calls': gmid_id+"/btn_calls",
    'lines_spinner': gmid_id+"/lines_spinner",
    'btn_dialer': gmid_id+"/btn_dialer",
    'input': gmid_id+"/et_input",
    'btn_call': gmid_id+"/btn_call",
    'swipe_up': gmid_id+"/tv_swipe_up",
    'btn_decline_call':  gmid_id+"/btn_decline_call"
}

UCC_id_msg = {
    'btn_chats': gmid_id+"/btn_chats",
    'btn_add_chat': gmid_id+"/btn_add_chat",
    'message_input': gmid_id+"/et_message_input",
    'input': gmid_id+"/et_input",
    'btn_call': gmid_id+"/btn_call",
    'swipe_up': gmid_id+"/tv_swipe_up",
    'btn_decline_call':  gmid_id+"/btn_decline_call"
}

UCC_xpath = {
    'Lab_Setting': "//*[@text='Lab Settings']",
    'Lab_Name': "//*[@text='Bangalore lab']",
    'ALLOW': "//*[@text='ALLOW']"
}