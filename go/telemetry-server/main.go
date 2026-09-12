package main

import (
	"encoding/json"
	"log"
	"math/rand"
	"net/http"
	"time"
)

type Telemetry struct {
	RobotID string  `json:"robotId"`
	Battery float64 `json:"battery"`
	Speed   float64 `json:"speed"`
	Heading float64 `json:"heading"`
	Status  string  `json:"status"`
}

func telemetryHandler(w http.ResponseWriter, r *http.Request) {
	packet := Telemetry{
		RobotID: "mini-lab-bot-01",
		Battery: 80 + rand.Float64()*20,
		Speed:   rand.Float64(),
		Heading: rand.Float64() * 360,
		Status:  "simulated",
	}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(packet)
}

func main() {
	rand.Seed(time.Now().UnixNano())
	http.HandleFunc("/telemetry", telemetryHandler)
	log.Println("telemetry server listening on http://localhost:8080/telemetry")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
