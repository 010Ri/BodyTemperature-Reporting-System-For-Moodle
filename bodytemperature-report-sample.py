# import
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

# elements for log in LMS (moodle) : ログインに必要な要素
USERNAME = 'USERNAME'
PASSWORD = 'PASSWORD'

# elements for filling form : 体温報告に必要な要素
BodyTemperature = input('今日の体温を入力してください(少数点第一位まで)：')
Others = '特になし'

# initializes 初期設定
error_flg = False
target_url = 'URL'  # moodle URL

# FUNCTION access : str == button name , click automatically and redirect to next page : access関数の定義：ボタンの名前をstrで指定し、クリックして次の画面へ進む
def access(str):
    try:
        access_button = driver.find_element_by_link_text(str)
        access_button.click()
        sleep(3)
    except Exception:
        error_flg = True
        print(str + 'ボタン押下時にエラーが発生しました。')

# turn on WebDriver : WebDriverの起動
options = Options()
options.add_argument('--headless')  # ここをコメントアウトすればヘッドレスモードを無効にできる
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver',options=options)
driver.get(target_url)
sleep(3)

# login process : ログイン処理

if error_flg is False:
    try:
        username_input = driver.find_element_by_name("username")
        username_input.send_keys(USERNAME)
        sleep(1)
 
        password_input = driver.find_element_by_name("password")
        password_input.send_keys(PASSWORD)
        sleep(1)
 
        username_input.submit()
        sleep(1)
        
    except Exception:
        print('ユーザー名、パスワード入力時にエラーが発生しました。')
        error_flg = True

# press take-exam-again button
if error_flg is False:
    try:
        again_button = driver.find_element_by_xpath('//form/button[@type="submit"]')
        again_button.click()
        sleep(3)
    except Exception:
        error_flg = True
        print('もう一度受験するボタン押下時にエラーが発生しました。')

# fill form
if error_flg is False:
    try:
        BodyTemperature_input = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/section[1]/div[1]/form/div/div[1]/div[2]/div[1]/div[2]/span/input')
        BodyTemperature_input.send_keys(BodyTemperature)
        sleep(1)
 
        others_input = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/section[1]/div[1]/form/div/div[3]/div[2]/div/div[2]/label/span/input')
        others_input.send_keys(Others)
        sleep(1)
        
    except Exception:
        print('体温の入力時にエラーが発生しました。')
        error_flg = True

if error_flg is False:
    try:
        Q_button = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/section[1]/div[1]/form/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/input[2]')
        driver.execute_script("arguments[0].click();",Q_button)
        sleep(3)
    except Exception:
        error_flg = True
        print('症状のボタン押下時にエラーが発生しました。')

# press finish-exam button
if error_flg is False:
    try:
        next_button = driver.find_element_by_name('next')
        next_button.click()
        sleep(3)
    except Exception:
        error_flg = True
        print('テストを終了する ...ボタン押下時にエラーが発生しました。')

if error_flg is False:
    try:
        submit_button = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/section[1]/div[1]/div[3]/div/div/form/button')
        submit_button.click()
        sleep(3)
    except Exception:
        error_flg = True
        print('すべての解答を送信して終了するボタン押下時にエラーが発生しました。')

if error_flg is False:
    try:
        check_button = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[2]/div/div[2]/input[1]')
        check_button.click()
        sleep(3)
    except Exception:
        error_flg = True
        print('「確認」すべての解答を送信して終了するボタン押下時にエラーが発生しました。')

if error_flg is False:
    access('レビューを終了する')

if error_flg is False:
    print('体温報告を完了しました。')

# putting away : 片付け
driver.close()
