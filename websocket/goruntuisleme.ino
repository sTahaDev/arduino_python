#include <ESP8266WiFi.h>
#include <WebSocketsServer.h>

const char *ssid = "Huseyin Sahin";
const char *password = "tahaburak0610";
WebSocketsServer webSocket = WebSocketsServer(81);

void webSocketEvent(uint8_t num, WStype_t type, uint8_t *payload, size_t length) {
  switch (type) {
    case WStype_TEXT:
      Serial.printf("[WebSocket] Received text: %s\n", payload);
      // Veri ile yapılacak işlemleri burada gerçekleştirin
      break;
  }
}

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
    Serial.println(WiFi.localIP());
  }

  webSocket.begin();
  webSocket.onEvent(webSocketEvent);
}

void loop() {
  webSocket.loop();
  // NodeMCU'nun diğer işlemlerini burada gerçekleştirin
}
