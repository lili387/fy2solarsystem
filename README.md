# Simulering av planet runt sol
För en enkel miljö där ni enkelt kan göra lite Först installera [Processing](https://processing.org/) addera python modul. Klona eller ladda ner detta repository, öppna [fy2solarsystem.pyde](fy2solarsystem.pyde) i Processing och klicka på playknappen. Relevanta sidor är 60-63 i boken.

## Processing
Vi använder Processing som ramverk för att det gör det lätt att utföra och rita upp simuleringen. Processing anroppar _setup()_ en gång och kommer där efter  många gånger per sekund anroppa _draw()_. I varje anropp till draw så uppdaterar vi positionen på planeterna och ritar om allt på skärmen.

## Uppgifter
1. Uppdatera planetens startvärden (position och hastighet) så att rörelsen blir en periodisk bana runt solen.
2. Enligt kepplers tredje lag så är T^3/R^2 konstant (s. 60 i Heureka). Vad är värdet denna kvot för denna planeten runt denna stjärnan. Du behöver uppdatera koden för att räkna ut T och R för din planetbana. T är omloppstiden och R är medelradien.  
3. **Extra:** lägg till en ny planet med en annan bana runt solen. Vad blir T^3/R^2 för denna planet?
4. Förklara vart och hur är den allmänna gravitations lagen är implementerad.
5. **Extra:** Lägg till en måne i omloppbana runt planeten.
