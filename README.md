<div align="center" style="display: flex; align-items: center; justify-content: center;">
  <picture>
    <source media="(prefers-color-scheme: dark" srcset="https://github.com/LarsG-2158052/CLOUD_Services/assets/146258020/285652eb-1553-462b-9168-17724bf44df3" width="100">
    <img src="https://github.com/LarsG-2158052/CLOUD_Services/assets/146258020/dc75c008-1ad5-4cf7-b743-39931e011ea3" width="100">
  </picture>
  <h1>MusicHub</h1>
</div>

## Deelservices
### 1. GraphQL:
- **Servicenaam:** InstrumentLibraryAPI
- **Programmeertaal:** JavaScript / Node.js
- **Programmeertaal uit de les:** Python

**Beschrijving:** 

Een GraphQL-service voor het kopen en verkopen van instrumenten. Muzikanten kunnen hun niet gebruikte instrumenten verkopen aan mensen die graag een 2de hands instrument willen kopen. Je kan instrumenten zoeken op onder andere het type, leeftijd, locatie en prijs. De GraphQL-service biedt een flexibele en efficiënte manier voor gebruikers om specifieke gegevens op te vragen, waardoor overbodige gegevens worden vermeden.

### 2. REST (Representational State Transfer):
- **Servicenaam:** EventBookingAPI
- **Programmeertaal:** Python
- **Programmeertaal uit de les:** PHP / Laravel Framework

**Beschrijving:** 

Een REST API voor het boeken van muziekevenementen. Muzikanten en evenementorganisatoren kunnen de API gebruiken om locaties voor muziekoptredens te beheren en te boeken. De API stelt gebruikers in staat om te zoeken naar komende evenementen, tickets te boeken en informatie te verkrijgen over de uitvoerders en het programma.

### 3. gRPC (Remote Procedure Call):
- **Servicenaam:** MessageAPI
- **Programmeertaal:** C#
- **Programmeertaal uit de les:** java

**Beschrijving:** 

Een gRPC-service voor het sturen van berichten tussen gebruikers.

### 4. SOAP (Simple Object Access Protocol):
- **Servicenaam:** SheetMusicAPI
- **Programmeertaal:** php
- **Programmeertaal uit de les:** C#

**Beschrijving:** 

Een SOAP service waarmee klassieke muzikanten toegang hebben tot een repository van digitale bladmuziek. Muzikanten kunnen zoeken naar specifieke composities, bladmuziek ophalen in verschillende formaten en zelfs hun eigen composities uploaden om te delen met anderen.

### 5. MQTT (Message Queuing Telemetry Transport):
- **Servicenaam:** RealTimeMusicUpdates
- **Programmeertaal:** Python
- **Programmeertaal uit de les:** Python

**Beschrijving:** 

Een op MQTT gebaseerde service voor het verzenden van realtime updates over nieuwe bladmuziek en/of populaire bladmuziek. Geabonneerde gebruikers ontvangen direct meldingen bij veranderingen of nieuwe inhoud.

### 6. Websockets:
- **Servicenaam:** CollaborativeMusicSession
- **Programmeertaal:** JavaScript / Node.js
- **Programmeertaal uit de les:** JavaScript / Node.js

**Beschrijving:** 

Een WebSocket-service voor het hosten van gezamenlijke muziek sessies. Muzikanten kunnen verbinding maken met de service, deelnemen aan een virtuele kamer waar ze met elkaar kunnen chatten en samen bladmuziek kunnen maken.

## Consumatie van services
De verschillende services zullen worden geconcumeerd in laravel met php. Ook zal de publieke API van openopus (https://github.com/openopus-org/openopus_api/tree/master) worden gebruikt om een database de hebben van verschillende componisten en hun composities. Authenticatie wordt gedaan met behulp van laravel breeze.

