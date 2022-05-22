import dingtalkchatbot.chatbot as cb


class DingRobot:

    def __init__(self, _webhook, _secret):
        self.dingTalk = cb.DingtalkChatbot(_webhook, _secret)

    def send_message(self, message):
        self.dingTalk.send_text(message)


if __name__ == "__main__":
    webhook = "https://oapi.dingtalk.com/robot/send?access_token" \
              "=81025a00a4861b5bd438ab926259d2fd19eca505b4b2c047537dfba52a02d464 "
    secret = "SEC42e45f4dff42f417ed0365b839f8f3d31385b9a17f3ccc9ae76d5b7ea6d95444"
    DingRobot(webhook, secret).send_message("test message")
