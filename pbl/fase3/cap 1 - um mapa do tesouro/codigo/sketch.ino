/**
 * @file farmtech_irrigacao.ino
 * @author Gemini
 * @brief Sistema de Irrigação Inteligente para a cultura de Milho (FarmTech - Fase 2).
 * * Este projeto simula um sistema de irrigação automatizado usando um ESP32 no Wokwi.
 * Ele monitora as condições do solo (umidade, pH e nutrientes NPK) e aciona
 * uma bomba d'água (representada por um relé) com base nas necessidades da cultura de milho.
 * * Componentes Simulados:
 * - Sensor de Umidade do Solo: DHT22 (medindo umidade do ar na simulação).
 * - Sensor de pH: Resistor Dependente de Luz (LDR).
 * - Sensores de Nutrientes (N, P, K): Três botões.
 * - Bomba d'água: Módulo Relé.
 */

// Inclusão da biblioteca para o sensor DHT
#include "DHT.h"

// --- Mapeamento dos Pinos do ESP32 ---

// Sensor de Umidade DHT22
#define DHT_PIN 15
#define DHT_TYPE DHT22
DHT dht(DHT_PIN, DHT_TYPE);

// Sensor de pH (LDR)
const int LDR_PIN = 34; // Pino de entrada analógica

// Sensores de Nutrientes (Botões)
const int BTN_N_PIN = 27; // Nitrogênio
const int BTN_P_PIN = 26; // Fósforo
const int BTN_K_PIN = 25; // Potássio

// Atuador (Bomba d'água via Relé)
const int RELE_PIN = 32;

// --- Parâmetros da Cultura (Milho) ---
const float UMIDADE_MIN_PARA_IRRIGAR = 55.0; // % - Aciona a irrigação se a umidade for menor que isso
const float UMIDADE_MAX_IDEAL = 75.0;       // % - Desliga a irrigação se a umidade for maior que isso
const float PH_MIN_IDEAL = 5.8;
const float PH_MAX_IDEAL = 6.8;

// Variável para armazenar o estado da bomba
bool bombaLigada = false;

void setup() {
  // Inicializa a comunicação serial para depuração
  Serial.begin(115200);
  Serial.println("--- Sistema de Irrigação Inteligente FarmTech ---");
  
  // Inicializa o sensor DHT
  dht.begin();

  // Configura os pinos dos botões como entrada com pull-up interno
  // O pull-up faz com que a leitura seja HIGH quando o botão não está pressionado
  pinMode(BTN_N_PIN, INPUT_PULLUP);
  pinMode(BTN_P_PIN, INPUT_PULLUP);
  pinMode(BTN_K_PIN, INPUT_PULLUP);

  // Configura o pino do relé como saída e garante que a bomba comece desligada
  pinMode(RELE_PIN, OUTPUT);
  digitalWrite(RELE_PIN, HIGH); // Módulos relé geralmente ativam em LOW
  bombaLigada = false;
}

void loop() {
  // --- Leitura dos Sensores ---

  // 1. Leitura do Sensor de Umidade (DHT22)
  float umidade = dht.readHumidity();

  // 2. Leitura do Sensor de pH (LDR)
  int valorLDR = analogRead(LDR_PIN);
  
  // CORREÇÃO FINAL: Mapeia o valor analógico do LDR de forma DIRETA e INTUITIVA.
  // Agora, mais luz (valor LDR alto, slider para a direita) resulta num pH ALTO (alcalino),
  // e menos luz (valor LDR baixo, slider para a esquerda) resulta num pH BAIXO (ácido).
  float phSimulado = map(valorLDR, 0, 4063, 0, 1400) / 100.0;

  // 3. Leitura dos Sensores de Nutrientes (Botões)
  // Como usamos INPUT_PULLUP, LOW significa que o botão está pressionado.
  bool nivelN_OK = (digitalRead(BTN_N_PIN) == LOW);
  bool nivelP_OK = (digitalRead(BTN_P_PIN) == LOW);
  bool nivelK_OK = (digitalRead(BTN_K_PIN) == LOW);

  // Verifica se a leitura do DHT foi bem-sucedida
  if (isnan(umidade)) {
    Serial.println("Falha ao ler o sensor DHT22!");
    delay(2000);
    return; // Pula o resto do loop se a leitura falhar
  }

  // --- Exibição dos Dados no Monitor Serial ---
  Serial.println("\n--- Monitoramento em Tempo Real ---");
  Serial.print("Umidade do Solo: ");
  Serial.print(umidade);
  Serial.println("%");

  Serial.print("pH Simulado: ");
  Serial.println(phSimulado);

  Serial.print("Nível de Nitrogênio (N): ");
  Serial.println(nivelN_OK ? "OK" : "Baixo");
  Serial.print("Nível de Fósforo (P): ");
  Serial.println(nivelP_OK ? "OK" : "Baixo");
  Serial.print("Nível de Potássio (K): ");
  Serial.println(nivelK_OK ? "OK" : "Baixo");

  // --- Lógica de Decisão para Irrigação ---

  // Condições para LIGAR a bomba
  bool umidadeBaixa = umidade < UMIDADE_MIN_PARA_IRRIGAR;
  bool phIdeal = phSimulado >= PH_MIN_IDEAL && phSimulado <= PH_MAX_IDEAL;
  bool nutrientesOK = nivelN_OK && nivelP_OK && nivelK_OK;

  // Condição para DESLIGAR a bomba
  bool umidadeAlta = umidade > UMIDADE_MAX_IDEAL;

  if (umidadeAlta) {
    // Desliga a bomba se a umidade máxima for atingida (prevenção de encharcamento)
    if (bombaLigada) {
      Serial.println("DECISÃO: Desligando a bomba. Umidade do solo atingiu o nível ideal.");
      digitalWrite(RELE_PIN, HIGH); // Desliga o relé
      bombaLigada = false;
    }
  } else if (umidadeBaixa && phIdeal && nutrientesOK) {
    // Liga a bomba somente se TODAS as condições ideais forem atendidas
    if (!bombaLigada) {
      Serial.println("DECISÃO: Ligando a bomba. Condições ideais para irrigação atendidas.");
      digitalWrite(RELE_PIN, LOW); // Liga o relé
      bombaLigada = true;
    }
  } else {
    // Desliga a bomba se qualquer uma das condições ideais não for atendida
    if (bombaLigada) {
      Serial.println("DECISÃO: Desligando a bomba. Condições para irrigação não são ideais.");
      digitalWrite(RELE_PIN, HIGH); // Desliga o relé
      bombaLigada = false;
    }
  }
  
  // Exibe o estado final da bomba
  Serial.print("Estado da Bomba: ");
  Serial.println(bombaLigada ? "LIGADA" : "DESLIGADA");

  // Aguarda 2 segundos antes da próxima leitura
  delay(2000);
}

