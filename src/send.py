from selenium.webdriver.common.keys import Keys

def send_message(rec, mes, browser):
    try:
        search_bar = browser.find_elements_by_xpath('//div[@contenteditable = "true"]')[0]          
        search_bar.send_keys(rec)
        search_bar.send_keys(Keys.ENTER)
        msg_bar = browser.find_elements_by_xpath('//div[@contenteditable = "true"]')[1]
        msgs = mes.split('\n')
        print(msgs)
        for m in msgs:
            msg_bar.send_keys(m)
            msg_bar.send_keys(Keys.SHIFT + Keys.ENTER)
            msg_bar.send_keys(Keys.SHIFT + Keys.ENTER)
        msg_bar.send_keys(Keys.ENTER)
        return 'Scorecard Sent Successfully'
    except Exception as e:
        print('Error: ', e)
        return 'Error While Sending Scorecard'  