from .baseapi import BaseAPI
from .errors import InvalidDataError

class FCMNotification(BaseAPI):
    def notify(
        self,
        fcm_token=None,
        notification_title=None,
        notification_body=None,
        notification_image=None,
        notification_sound=None,  # Added sound parameter
        data_payload=None,
        topic_name=None,
        topic_condition=None,
        android_config=None,
        webpush_config=None,
        apns_config=None,
        fcm_options=None,
        dry_run=False,
        timeout=120,
    ):
        """
        Send push notification to a single device

        Args:
            fcm_token (str, optional): FCM device registration ID
            notification_title (str, optional): Message title to display in the notification tray
            notification_body (str, optional): Message string to display in the notification tray
            notification_image (str, optional): Icon that appears next to the notification
            notification_sound (str, optional): Sound to play when the notification is received
            data_payload (dict, optional): Arbitrary key/value payload, which must be UTF-8 encoded
            topic_name (str, optional): Name of the topic to deliver messages to e.g. "weather"
            topic_condition (str, optional): Condition to broadcast a message to
            android_config (dict, optional): Android specific options for messages
            apns_config (dict, optional): Apple Push Notification Service specific options
            webpush_config (dict, optional): Webpush protocol options
            fcm_options (dict, optional): Platform independent options
            timeout (int, optional): Set time limit for the request

        Returns:
            dict: name (str) - The identifier of the message sent
        """
        payload = self.parse_payload(
            fcm_token=fcm_token,
            notification_title=notification_title,
            notification_body=notification_body,
            notification_image=notification_image,
            notification_sound=notification_sound,  # Added sound parameter
            data_payload=data_payload,
            topic_name=topic_name,
            topic_condition=topic_condition,
            android_config=android_config,
            apns_config=apns_config,
            webpush_config=webpush_config,
            fcm_options=fcm_options,
            dry_run=dry_run,
        )
        response = self.send_request(payload, timeout)
        return self.parse_response(response)

    def async_notify_multiple_devices(self, params_list=None, timeout=5):
        """
        Sends push notification to multiple devices with personalized templates

        Args:
            params_list (list): list of parameters (the same as notify_multiple_devices)
            timeout (int, optional): set time limit for the request
        """
        if params_list is None:
            params_list = []

        return self.send_async_request(params_list=params_list, timeout=timeout)
