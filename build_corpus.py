"""
Original agriculture training corpus generator.
Produces factual paragraphs + Q&A pairs across:
hydroponics, aeroponics, aquaponics, aquaculture, dairy farming, microgreens.
All text is written fresh (template + fact substitution), not copied from any source.
"""
import random
random.seed(42)

lines = []

def add_para(text):
    lines.append(text.strip() + "\n")

def add_qa(q, a):
    lines.append(f"Q: {q}\nA: {a}\n")

# ---------------------------------------------------------------
# HYDROPONICS
# ---------------------------------------------------------------
add_para("""Hydroponics is a method of growing plants without soil, using a nutrient-rich
water solution to deliver minerals directly to the roots. Common inert growing media
include rockwool, perlite, clay pebbles, coco coir, and vermiculite. Because nutrients
are delivered directly in dissolved form, plants often grow faster than in soil,
provided oxygen, pH, and nutrient concentration are all managed correctly.""")

add_para("""The most common hydroponic systems are Deep Water Culture (DWC), Nutrient Film
Technique (NFT), Ebb and Flow (flood and drain), Drip systems, and Wick systems. DWC
suspends roots directly in an oxygenated nutrient solution. NFT flows a thin film of
nutrient solution continuously over the roots. Drip systems deliver nutrient solution
directly at the base of each plant on a timed cycle.""")

add_para("""For most leafy greens grown hydroponically, the ideal pH range is between 5.5 and
6.5. Outside this range, nutrient uptake becomes inefficient even if the correct
nutrients are present in solution, because certain minerals become chemically locked
and unavailable to the roots at high or low pH.""")

add_para("""Electrical conductivity (EC) or total dissolved solids (TDS) measures the strength
of the nutrient solution. Leafy greens like lettuce typically prefer an EC of 1.2 to
1.8 mS/cm (600 to 900 ppm TDS), while fruiting crops like tomatoes need higher EC,
often 2.0 to 3.5 mS/cm, especially during the flowering and fruiting stage.""")

add_para("""Root rot is one of the most common hydroponic problems, usually caused by low
dissolved oxygen in the nutrient solution, warm water temperatures above 24 degrees
Celsius, or poor circulation. Symptoms include brown, slimy roots and a foul smell.
Prevention includes using air stones for oxygenation, keeping reservoir temperatures
cool, and cleaning the system between crop cycles.""")

add_para("""Nutrient deficiencies show up visually before yield is affected. Nitrogen
deficiency causes older leaves to yellow first. Iron deficiency causes yellowing
between the veins of new leaves while the veins stay green. Calcium deficiency often
appears as tip burn on lettuce or blossom end rot on tomatoes and peppers.""")

add_para("""A hydroponic nutrient solution should generally be replaced every one to two weeks,
even if TDS readings look acceptable, because plants absorb nutrients unevenly. Some
elements get depleted faster than others, which can shift the ratio of the solution
even while total dissolved solids appear stable.""")

add_para("""Light is as important as nutrients in hydroponics. Leafy greens typically need 14
to 16 hours of light per day at moderate intensity, while fruiting crops like tomatoes
and cucumbers need higher light intensity, often provided through LED grow lights in
indoor systems, with a daily light integral tuned to the crop stage.""")

qa_hydro = [
    ("What is hydroponics?", "Hydroponics is growing plants without soil, using a water-based nutrient solution to feed the roots directly."),
    ("What pH is best for hydroponic lettuce?", "A pH between 5.5 and 6.5 is ideal for most hydroponic leafy greens including lettuce."),
    ("My hydroponic system pH is 4.2, what should I do?", "A pH of 4.2 is too acidic for almost all hydroponic crops. Add a pH-up solution gradually and retest until the pH reaches 5.5 to 6.5."),
    ("What causes root rot in hydroponics?", "Root rot is usually caused by low dissolved oxygen, warm reservoir water above 24 degrees Celsius, or poor circulation in the nutrient solution."),
    ("What TDS should I use for lettuce?", "Lettuce grows well at a TDS of roughly 600 to 900 ppm, equivalent to an EC of 1.2 to 1.8 mS/cm."),
    ("What TDS should I use for tomatoes?", "Tomatoes generally need higher TDS during fruiting, often 1000 to 1750 ppm, equivalent to 2.0 to 3.5 mS/cm EC."),
    ("Why are my hydroponic plant's older leaves turning yellow?", "Yellowing of older leaves first is a classic sign of nitrogen deficiency in the nutrient solution."),
    ("How often should I change hydroponic nutrient solution?", "Replace the nutrient solution every one to two weeks even if the TDS reading looks fine, since nutrient ratios shift as plants absorb elements unevenly."),
    ("What growing medium is used in hydroponics?", "Common inert media include rockwool, perlite, clay pebbles, coco coir, and vermiculite."),
    ("What is NFT in hydroponics?", "NFT stands for Nutrient Film Technique, where a thin film of nutrient solution flows continuously over plant roots."),
    ("What is DWC in hydroponics?", "DWC stands for Deep Water Culture, where plant roots are suspended directly in an oxygenated nutrient solution."),
    ("How many hours of light do hydroponic leafy greens need?", "Leafy greens typically need 14 to 16 hours of light per day at moderate intensity."),
    ("What does calcium deficiency look like in hydroponics?", "Calcium deficiency often shows as tip burn on lettuce leaves or blossom end rot on tomatoes and peppers."),
    ("Why does my nutrient solution smell bad?", "A foul smell in the reservoir usually indicates root rot or bacterial buildup from stagnant, low-oxygen water."),
    ("What is EC in hydroponics?", "EC stands for electrical conductivity, a measurement of the nutrient concentration dissolved in the water."),
]
for q, a in qa_hydro:
    add_qa(q, a)

# ---------------------------------------------------------------
# AEROPONICS
# ---------------------------------------------------------------
add_para("""Aeroponics grows plants with their roots suspended in air inside an enclosed
chamber, misted periodically with a fine nutrient solution spray. Because roots are
exposed to more oxygen than in hydroponics or soil, aeroponic systems can produce
faster growth rates when misting timing and droplet size are correctly managed.""")

add_para("""In a vertical aeroponic tower, plants are placed in netted cups along the outside
of a cylindrical column, with a pump misting the internal chamber at set intervals,
typically every few minutes for a few seconds. Water that is not absorbed drips back
down and recirculates through the reservoir.""")

add_para("""Because aeroponic roots have no growing medium to buffer against nutrient swings,
water quality matters more than in soil or even hydroponics. Reverse osmosis (RO)
water is usually preferred as the base, since high mineral content or contaminants
in tap water can clog fine mist nozzles and disrupt the nutrient balance.""")

add_para("""Aeroponic TDS targets generally increase through the crop cycle. Early growth
stages typically target 300 to 500 ppm, vegetative growth targets 600 to 750 ppm,
and flowering or fruiting stages may need 750 to 1000 ppm along with a bloom-specific
nutrient blend.""")

add_para("""The biggest risk in aeroponics is pump or nozzle failure. Because roots have no
soil or medium retaining moisture, even a short interruption in misting, sometimes
just 30 to 60 minutes, can cause roots to dry out and the plant to wilt rapidly.
Redundant pumps or alarms on mist cycles are common risk mitigations.""")

qa_aero = [
    ("What is aeroponics?", "Aeroponics is a growing method where plant roots hang in air inside a chamber and are periodically misted with a nutrient solution, without any soil or solid growing medium."),
    ("What water should I use for aeroponics?", "Reverse osmosis (RO) water is preferred for aeroponics because high mineral content or contaminants in tap water can clog fine mist nozzles."),
    ("What TDS should I use in early aeroponic growth?", "Early growth stages typically target a TDS of 300 to 500 ppm."),
    ("What TDS should I use during aeroponic flowering?", "During flowering or fruiting, aeroponic TDS targets are usually 750 to 1000 ppm with a bloom-specific nutrient blend."),
    ("What is the biggest risk in aeroponic systems?", "Pump or nozzle failure is the biggest risk, since roots can dry out and the plant can wilt within 30 to 60 minutes without misting."),
    ("How often does an aeroponic system mist the roots?", "Typically every few minutes for a few seconds, though exact timing depends on chamber humidity and root size."),
    ("Why is aeroponics faster growing than soil?", "Aeroponic roots are exposed to more oxygen than roots in soil or standing water, which can accelerate nutrient uptake and growth when misting is well managed."),
]
for q, a in qa_aero:
    add_qa(q, a)

# ---------------------------------------------------------------
# AQUAPONICS
# ---------------------------------------------------------------
add_para("""Aquaponics combines aquaculture (raising fish) with hydroponics (growing plants
without soil) in one recirculating system. Fish waste, primarily ammonia, is
converted by nitrifying bacteria into nitrite and then nitrate, which plants absorb
as fertilizer. Water is then returned to the fish tank, cleaned of excess nutrients.""")

add_para("""The nitrogen cycle is the core biological process in aquaponics. Ammonia from
fish waste is converted to nitrite by Nitrosomonas bacteria, and nitrite is converted
to nitrate by Nitrobacter bacteria. This biofilter step usually takes several weeks
to establish in a new system, a process called cycling, before fish stocking density
can be increased safely.""")

add_para("""Common fish species used in aquaponics include tilapia, catfish, and koi for
warmer systems, and trout for cooler water systems. Tilapia is popular because it
tolerates a wide range of water quality conditions and grows quickly in warm water
between 24 and 30 degrees Celsius.""")

add_para("""Because aquaponics relies on live fish and living bacteria colonies, water
parameters must stay within safer, narrower ranges than hydroponics alone. Ammonia
and nitrite should stay near zero ppm once the system is cycled, since both are toxic
to fish even at low concentrations. Nitrate can be allowed to build up somewhat higher
since plants consume it.""")

add_para("""Aquaponic systems generally cannot use the same synthetic nutrient supplements as
hydroponics, since these can harm fish. Instead, growers rely on fish feed quality
and occasional iron or potassium supplementation, since fish waste alone often
under-supplies these two elements for heavy-feeding plants.""")

qa_aqua_ponic = [
    ("What is aquaponics?", "Aquaponics is a system that combines raising fish with growing plants without soil, where fish waste is converted by bacteria into nutrients the plants absorb."),
    ("What is the nitrogen cycle in aquaponics?", "Fish waste produces ammonia, which Nitrosomonas bacteria convert to nitrite, and Nitrobacter bacteria then convert to nitrate, which plants use as fertilizer."),
    ("What fish are commonly used in aquaponics?", "Tilapia, catfish, and koi are common in warmer systems, while trout is used in cooler water systems."),
    ("What ammonia level is safe in aquaponics?", "Once a system is fully cycled, ammonia should stay near zero ppm, since it is toxic to fish even at low concentrations."),
    ("Can I use hydroponic nutrients in aquaponics?", "No, standard synthetic hydroponic nutrients can harm fish. Aquaponic growers instead rely on fish feed and occasional iron or potassium supplementation."),
    ("Why does a new aquaponics system need cycling?", "Cycling allows nitrifying bacteria colonies (Nitrosomonas and Nitrobacter) to establish, which is necessary before fish stocking density can be safely increased."),
    ("What temperature does tilapia prefer?", "Tilapia grows quickly in warm water between 24 and 30 degrees Celsius."),
]
for q, a in qa_aqua_ponic:
    add_qa(q, a)

# ---------------------------------------------------------------
# AQUACULTURE
# ---------------------------------------------------------------
add_para("""Aquaculture is the farming of aquatic organisms, including fish, shrimp, and
shellfish, in controlled environments such as ponds, tanks, or cages. It is one of
the fastest growing food production sectors globally, and countries like India are
major producers of farmed shrimp, particularly Litopenaeus vannamei (vannamei shrimp).""")

add_para("""Water quality monitoring is central to aquaculture success. Key parameters include
dissolved oxygen, pH, temperature, ammonia, nitrite, and salinity for brackish or
marine species. Dissolved oxygen below 3 mg/L is stressful for most fish and shrimp,
and prolonged low oxygen can cause mass mortality events.""")

add_para("""For vannamei shrimp farming, ideal water parameters are typically pH 7.5 to 8.5,
dissolved oxygen above 4 mg/L, salinity between 10 and 25 ppt, and temperature
between 28 and 32 degrees Celsius. Sudden changes in any of these parameters, even
within the acceptable range, can stress shrimp and increase disease susceptibility.""")

add_para("""Common aquaculture diseases include White Spot Syndrome Virus (WSSV) in shrimp,
which causes rapid mortality and has no cure, making biosecurity and water quality
management the primary prevention strategy. Early warning signs include lethargy,
reduced feeding, and white spots on the shell.""")

add_para("""Aeration is critical in aquaculture ponds because photosynthesis by algae during
the day produces oxygen, but at night, algae and other organisms consume oxygen
through respiration, often causing the lowest dissolved oxygen levels just before
dawn. Paddlewheel aerators or diffused aeration systems are used to prevent oxygen
crashes during this period.""")

add_para("""Feed conversion ratio (FCR) measures how efficiently farmed aquatic animals convert
feed into body weight. A lower FCR indicates more efficient farming. Typical FCR for
well-managed vannamei shrimp farming is between 1.2 and 1.6, meaning 1.2 to 1.6 kg
of feed produces 1 kg of shrimp biomass.""")

qa_aquaculture = [
    ("What is aquaculture?", "Aquaculture is the farming of aquatic organisms such as fish, shrimp, and shellfish in controlled environments like ponds, tanks, or cages."),
    ("What is the ideal pH for vannamei shrimp farming?", "Vannamei shrimp farming generally targets a pH range of 7.5 to 8.5."),
    ("My aquaculture pond pH is 4.2, what should I do?", "A pH of 4.2 is dangerously low for most aquaculture species and can cause severe stress or mortality. Add an alkaline buffer such as agricultural lime gradually, retest frequently, and avoid sudden large pH swings."),
    ("What dissolved oxygen level is safe for fish and shrimp?", "Dissolved oxygen should generally stay above 4 mg/L; levels below 3 mg/L are stressful and can lead to mortality if prolonged."),
    ("Why is dissolved oxygen lowest before dawn in aquaculture ponds?", "Algae and other organisms consume oxygen through respiration at night without producing any through photosynthesis, causing oxygen to drop to its lowest point just before sunrise."),
    ("What is White Spot Syndrome Virus?", "WSSV is a viral disease in shrimp causing rapid mortality with no cure, making biosecurity and water quality management the main prevention strategy."),
    ("What is FCR in aquaculture?", "FCR, or Feed Conversion Ratio, measures how much feed is needed to produce one unit of body weight gain; lower FCR means more efficient farming."),
    ("What salinity is best for vannamei shrimp?", "Vannamei shrimp are typically farmed at a salinity of 10 to 25 ppt."),
]
for q, a in qa_aquaculture:
    add_qa(q, a)

# ---------------------------------------------------------------
# DAIRY FARMING
# ---------------------------------------------------------------
add_para("""Dairy farming involves raising cattle or buffalo for milk production, requiring
attention to nutrition, housing, health monitoring, and breeding management. Milk
yield and quality depend heavily on balanced feed, clean water access, and stress-free
housing conditions.""")

add_para("""A dairy cow's body temperature normally ranges from 38.0 to 39.3 degrees Celsius.
A sustained temperature above this range can indicate infection, mastitis, or heat
stress, while a drop below normal can indicate metabolic disorders such as milk
fever, especially in the days immediately following calving.""")

add_para("""Mastitis is one of the most common and costly dairy diseases, an inflammation of
the udder usually caused by bacterial infection. Early signs include swelling, heat,
and hardness in the udder, abnormal milk (clots or discoloration), and a drop in
milk yield. Regular udder health checks and clean milking practices reduce risk.""")

add_para("""Rumination time, the time a cow spends chewing cud, is a strong indicator of
health and comfort. Healthy dairy cows typically ruminate for 7 to 10 hours per day.
A significant drop in rumination time often precedes visible signs of illness by
12 to 24 hours, making it a useful early warning signal in sensor-based monitoring.""")

add_para("""Body condition scoring (BCS) is used to assess a dairy animal's fat reserves on
a scale, commonly 1 to 5. A BCS around 3 to 3.5 at calving is generally considered
ideal; scores that are too low indicate undernutrition, while scores too high
increase the risk of metabolic disorders after calving.""")

add_para("""Heat detection is critical for dairy breeding efficiency. Signs of estrus (heat)
include increased activity, mounting behavior, clear mucus discharge, and a drop in
milk yield on the day of heat. Missing heat detection windows, typically lasting
12 to 18 hours, directly increases the calving interval and reduces farm profitability.""")

qa_dairy = [
    ("What is the normal body temperature of a dairy cow?", "A healthy dairy cow's body temperature normally ranges from 38.0 to 39.3 degrees Celsius."),
    ("What is mastitis?", "Mastitis is inflammation of the udder, usually caused by bacterial infection, showing as swelling, heat, hardness, and abnormal milk."),
    ("How many hours per day should a healthy cow ruminate?", "Healthy dairy cows typically ruminate, or chew cud, for 7 to 10 hours per day."),
    ("Why is rumination time useful for health monitoring?", "A drop in rumination time often precedes visible signs of illness by 12 to 24 hours, making it a good early warning indicator."),
    ("What is body condition score in dairy cattle?", "Body condition score (BCS) rates an animal's fat reserves, usually on a 1 to 5 scale, with 3 to 3.5 considered ideal at calving."),
    ("How do I detect heat in a dairy cow?", "Signs of heat include increased activity, mounting behavior, clear mucus discharge, and a temporary drop in milk yield."),
    ("What causes milk fever in dairy cows?", "Milk fever is a metabolic disorder linked to low blood calcium, most common in the days immediately following calving."),
]
for q, a in qa_dairy:
    add_qa(q, a)

# ---------------------------------------------------------------
# MICROGREENS
# ---------------------------------------------------------------
add_para("""Microgreens are young vegetable greens harvested just after the first true leaves
appear, typically 7 to 21 days after germination depending on the crop. Common
microgreen crops include fenugreek, radish, mustard, sunflower, pea shoots, and
broccoli, each with different germination and growth timelines.""")

add_para("""Growing media choice affects both yield and ease of harvest. Pure cocopeat retains
moisture well and is common for home growers, while blends such as 80 percent
cocopeat with 20 percent vermicompost can improve nutrient availability and root
development, often resulting in slightly higher biomass compared to pure cocopeat.""")

add_para("""Fenugreek microgreens typically germinate within 2 to 3 days and are ready for
harvest around 8 to 12 days after sowing. They prefer consistent moisture without
waterlogging, and good air circulation to prevent fungal issues during the humid
early growth stage.""")

add_para("""Damping-off is the most common microgreens disease, a fungal issue causing
seedlings to collapse at the soil line shortly after germination. It is caused by
excess moisture, poor air circulation, and overcrowded seeding. Prevention includes
avoiding overwatering, ensuring airflow, and not oversowing seeds too densely.""")

add_para("""Blackout periods, where trays are covered for the first 2 to 4 days after sowing,
help many microgreens germinate more evenly by mimicking being under soil, before
being uncovered and moved into light for the true-leaf growth stage.""")

add_para("""Light requirements for microgreens are lower than for mature plants, since the
growth cycle is short and stored seed energy powers much of early growth. Still,
12 to 16 hours of light per day during the post-blackout stage produces stronger
stems and better color compared to low-light conditions.""")

qa_micro = [
    ("What are microgreens?", "Microgreens are young vegetable greens harvested shortly after the first true leaves appear, usually 7 to 21 days after germination."),
    ("How long do fenugreek microgreens take to grow?", "Fenugreek microgreens typically germinate in 2 to 3 days and are ready for harvest around 8 to 12 days after sowing."),
    ("What is damping-off in microgreens?", "Damping-off is a fungal disease causing seedlings to collapse at the soil line, caused by excess moisture, poor airflow, and overcrowded seeding."),
    ("What growing medium is best for microgreens?", "Pure cocopeat is common and retains moisture well, while an 80/20 cocopeat-to-vermicompost blend can improve nutrient availability and slightly increase biomass."),
    ("How do I grow microgreens on cocopeat?", "Fill a shallow tray with 2 to 3 cm of moistened cocopeat, spread seeds evenly and densely on top, mist lightly, cover for the blackout period, then move into light once shoots emerge, keeping the cocopeat moist but never waterlogged."),
    ("What is a blackout period in microgreens growing?", "A blackout period covers trays for the first 2 to 4 days after sowing to mimic being under soil, helping many crops germinate more evenly."),
    ("How much light do microgreens need after blackout?", "Microgreens typically need 12 to 16 hours of light per day during the true-leaf growth stage after the blackout period ends."),
    ("Why are my microgreens turning yellow?", "Yellowing can indicate insufficient light after the blackout stage, overwatering, or nutrient-poor growing medium; check light exposure and moisture levels first."),
    ("Should I water cocopeat trays every day?", "Cocopeat should be kept evenly moist, usually needing a light misting once or twice a day, but never left soggy since standing water encourages damping-off and root rot in microgreens trays."),
    ("Is cocopeat or vermicompost blend better for microgreens yield?", "An 80 percent cocopeat and 20 percent vermicompost blend often produces slightly higher biomass than pure cocopeat because it supplies more available nutrients during the short growth cycle."),
    ("How deep should the cocopeat layer be for microgreens trays?", "A cocopeat layer of about 2 to 3 centimeters is usually enough to hold consistent moisture for microgreens without becoming waterlogged."),
]
for q, a in qa_micro:
    add_qa(q, a)

# ---------------------------------------------------------------
# Write out, shuffled in blocks to mix domains, repeated for volume
# ---------------------------------------------------------------
random.shuffle(lines)
corpus = "\n".join(lines)

# Repeat with reshuffling to build volume without pure duplication order
all_text = []
base_lines = lines[:]
for _ in range(6):
    random.shuffle(base_lines)
    all_text.append("\n".join(base_lines))

final_text = "\n\n".join(all_text)

with open("agri_corpus.txt", "w", encoding="utf-8") as f:
    f.write(final_text)

print("Total characters:", len(final_text))
print("Total lines (facts+qa):", len(lines))
print("Approx size KB:", len(final_text.encode('utf-8')) / 1024)
