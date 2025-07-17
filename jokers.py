from collections import defaultdict


jokers_dict = defaultdict(lambda: "missing")
jokers_dict.update(
    {
        "Joker": "+4 Mult",
        "Chaos the Clown": "1 free Reroll per shop",
        "Jolly Joker": "+8 Mult if played hand contains a Pair",
        "Zany Joker": "+12 Mult if played hand contains a Three of a Kind",
        "Mad Joker": "+10 Mult if played hand contains a Two Pair",
        "Crazy Joker": "+12 Mult if played hand contains a Straight",
        "Droll Joker": "+10 Mult if played hand contains a Flush",
        "Half Joker": "+20 Mult if played hand contains 3 or fewer cards",
        "Merry Andy": "+3 discards, -1 hand size",
        "Stone Joker": "This Joker gains +25 Chips for each Stone Card in your full deck ",
        "Juggler": "+1 hand size",
        "Drunkard": "+1 discard",
        "Acrobat": "X3 Mult on final hand of round ",
        "Sock and Buskin": "Retrigger all played face cards",
        "Mime": "Retrigger all card held in hand abilities",
        "Credit Card": "Go up to -$20 in debt",
        "Greedy Joker": "Played cards with Diamond suit give +3 Mult when scored",
        "Lusty Joker": "Played cards with Heart suit give +3 Mult when scored",
        "Wrathful Joker": "Played cards with Spade suit give +3 Mult when scored",
        "Gluttonous Joker": "Played cards with Club suit give +3 Mult when scored",
        "Troubadour": "+2 hand size, -1 hands per round",
        "Banner": "+30 Chips for each remaining discard ",
        "Mystic Summit": "+15 Mult when 0 discards remaining ",
        "Marble Joker": "Adds one Stone card to deck when Blind is selected",
        "Loyalty Card": "X4 Mult every 6 hands played (0 remaining)",
        "Hack": "Retrigger each played 2, 3, 4, or 5",
        "Misprint": "+0 - +23 Mult",
        "Steel Joker": "This Joker gains X0.2 Mult for each Steel Card in your full deck ",
        "Raised Fist": "Adds double the rank of lowest card held in hand to Mult",
        "Golden Joker": "Earn $4 at end of round",
        "Blueprint": "Copies ability of Joker to the right",
        "Glass Joker": "This Joker gains X0.75 Mult for every Glass Card that is destroyed ",
        "Scary Face": "Played face cards give +30 Chips when scored",
        "Abstract Joker": "+3 Mult for each Joker card ",
        "Delayed Gratification": "Earn $2 per discard if no discards are used by end of the round",
        "Golden Ticket": "Played Gold cards earn $4 when scored",
        "Pareidolia": "All cards are considered Face cards",
        "Cartomancer": "Create a Tarot card when Blind is selected (Must have room)",
        "Even Steven": "Played cards with even rank give +4 Mult when scored (10, 8, 6, 4, 2)",
        "Odd Todd": "Played cards with odd rank give +31 Chips when scored (A, 9, 7, 5, 3)",
        "Wee Joker": "This Joker gains +8 Chips when each played 2 is scored ",
        "Business Card": "Played Face cards have a 1 in 2 chance to give $2 when scored",
        "Supernova": "Adds the number of times poker hand has been played to Mult ",
        "Mr. Bones": "Prevents Death if chips scored are at least 25% of required chips self destructs",
        "Seeing Double": "X2 Mult if played hand has a scoring Club card and a scoring card of any other suit",
        "The Duo": "X2 Mult if played hand contains a Pair",
        "The Trio": "X3 Mult if played hand contains a Three of a Kind",
        "The Family": "X4 Mult if played hand contains a Four of a Kind",
        "The Order": "X3 Mult if played hand contains a Straight",
        "The Tribe": "X2 Mult if played hand contains a Flush",
        "8 Ball": "1 in 4 chance for each played 8 to create a Tarot card when scored (Must have room)",
        "Fibonacci": "Each plaed Ace, 2, 3, 5, or 8 gives +8 Mult when scored",
        "Joker Stencil": "X1 Mult for each empty Joker slot Joker stencil included ",
        "Space Joker": "1 in 4 chane to upgrade level of played poker hand",
        "Matador": "Earn $8 if played hand triggers the Boss Blind ability",
        "Ceremonial Dagger": "When Blind is selected, destroy Joker to the right and permanently add double its sell value to this Mult ",
        "Showman": "Joker, Tarot, Planet, and Spectral cards may appear multiple times",
        "Fortune Teller": "+1 Mult per Tarot card used this run ",
        "Hit the Road": "This Joker gains X0.5 Mult per discarded Jack this round ",
        "Swashbuckler": "Adds the sell value of all other owned Jokers to Mult",
        "Flower Pot": "X3 Mult if poker hand contains a Diamond card, Club card, Heart card, and Spade card",
        "Ride the Bus": "This Joker gains +1 Mult per consecutive hand played without a scoring face card ",
        "Shoot the Moon": "+13 Mult for each Queen held in hand",
        "Scholar": "Played Aces give +20 Chips and +4 Mult when scored",
        "Smeared Joker": "Heart and Diamond count as the same suit, Spade and Club count as the same suit",
        "Oops! All 6s": "Double all listed probabilities (ex: 1 in 3 -> 2 in 3)",
        "Four Fingers": "All Flushes and Straights can be made with 4 cards",
        "Gros Michel": "+15 Mult 1 in 6 chance this card is destroyed at the end of the round",
        "Stuntman": "+250 Chips, -2 hand size",
        "Hanging Chad": "Retrigger first played card used in scoring 2 additional times",
        "Driver's License": "X3 Mult if you have at least 16 Enhanced cards in your full deck ",
        "Invisible Joker": "After 2 rounds, sell this card to duplicate a random Joker ",
        "Astronomer": "All Planet cards and Celestial Packs in the shop are free",
        "Burnt Joker": "Upgrade the level of the first discarded poker hand each round",
        "Dusk": "Retrigger all played cards in final hand of round ",
        "Throwback": "X0.25 Mult for each Blind skipped this run ",
        "The Idol": "Each played 2 of Hearts gives X2 Mult when scored Card changes every round",
        "Brainstorm": "Copies the ability of the leftmost Joker",
        "Satellite": "Earn $1 at the end of round per unique Planet card used this run ",
        "Rough Gem": "Played cards with Diamond suit earn $1 when scored",
        "Bloodstone": "1 in 2 chance for played cards with Heart suit to give X1.5 Mult when scored",
        "Arrowhead": "Played cards with Spade suit give +50 Chips when scored",
        "Onyx Agate": "Played cards with Club suit give +7 Mult when scored",
        "Canio": "Gains X1 Mult when a face card is destroyed ",
        "Triboulet": "Played Kings and Queens each give X2 Mult when scored",
        "Yorick": "This Joker gains X1 Mult every 23 [23] cards discarded ",
        "Chicot": "Disables effect of every Boss Blind",
        "Perkeo": "Creates a Negative copy of 1 random consumable card in your possession at the end of the shop",
        "Certificate": "When round begins, add a random playing card with a random seal to your hand",
        "Bootstraps": "+2 Mult for every $5 you have ",
        "Egg": "Gains $3 of sell value at end of round",
        "Burglar": "When Blind is selected, gain +3 Hands and lose all discards",
        "Blackboard": "X3 Mult if all cards held in hand are Spade or Club",
        "Runner": "Gains +15 Chips if played hand contains a Straight ",
        "Ice Cream": "+100 Chips -5 Chips for every hand played",
        "DNA": "If first hand of round has only 1 card, add a permanent copy to deck and draw it to hand",
        "Splash": "Every  played card counts in scoring",
        "Blue Joker": "+2 Chips for each remaining card in Deck ",
        "Sixth Sense": "If first hand of round is a single 6, destroy it and create a Spectral card (Must have room)",
        "Constellation": "This Joker gains X0.1 Mult per Planet card used ",
        "Hiker": "Every played card permanently gains +5 Chips when scored",
        "Faceless Joker": "Earn $5 if 3 or more face cards are discarded at the same time",
        "Green Joker": "+1 Mult per hand played -1 Mult per discard ",
        "Superposition": "Create a Tarot card if poker hand contains an Ace and a Straight (Must have room)",
        "To Do List": "Earn $4 if poker hand is a Pair, poker hand changes at end of round",
        "Cavendish": "X3 Mult 1 in 1000 chance this card is destroy at end of round",
        "Card Sharp": "X3 Mult if played poker hand has already been played this round ",
        "Red Card": "This Joker gains +3 Mult when any Booster Pack is skipped ",
        "Madness": "When Small Blind or Big Blind is selected, gain X0.5 Mult and destroy a random Joker ",
        "Square Joker": "This Joker gains +4 Chips if played hand has exactly 4 card ",
        "Séance": "If poker hand is a Straight Flush, craeate a random Spectral card (Must have room)",
        "Riff-raff": "When Blind is selected, create 2 Common Jokers (Must have room)",
        "Vampire": "This Joker gains X0.1 Mult per scoring Enhanced card played, removes card Enhancement ",
        "Shortcut": "Allows Straights to be made with gaps of 1 rank (ex: 10 8 6 5 3)",
        "Hologram": "This Joker gains X0.25 Mult  per playing card added to your deck ",
        "Vagabond": "Create a Tarot card if hand is played with $4 or less",
        "Baron": "Each King held in hand gives X1.5 Mult",
        "Cloud 9": "Earn $1 for each 9 in your full deck at end of round ",
        "Rocket": "Earn $1 at end of round. Gains $2 when Boss Blind is defeated",
        "Obelisk": "This Joker gains X0.2 Mult per consecutive hand played without playing your must played poker hand ",
        "Midas Mask": "All played face cards become Gold cards when scored",
        "Luchador": "Sell this card to disable the current Boss Blind",
        "Photograph": "First played face card gives X2 Mult when scored",
        "Gift Card": "Add $1 of sell value to every Joker and Consumable card at end of round",
        "Turtle Bean": "+5 hand size, reduces by 1 every round",
        "Erosion": "+4 Mult for each card below 52 in your full deck ",
        "Reserved Parking": "Each face card held in hand has a 1 in 2 chance to give $1",
        "Mail-In Rebate": "Earn $5 for each discarded 2, rank changes every round",
        "To the Moon": "Earn an extra $1 of interest for every $5 you have at end of round",
        "Hallucination": "1 in 2 chance to create a Tarot card when any Booster Pack is opened (Must have room)",
        "Sly Joker": "+50 Chips if played hand contains a Pair",
        "Wily Joker": "+100 Chips if played hand contains a Three of a Kind",
        "Clever Joker": "+80 Chips if played hand contains a Two Pair",
        "Devious Joker": "+100 Chips if played hand contains a Straight",
        "Crafty Joker": "+80 Chips if played hand contains a Flush",
        "Lucky Cat": "This Joker gains X0.25 Mult each time a Lucky card successfully triggers",
        "Baseball Card": "Uncommon Jokers each give X1.5 Mult",
        "Bull": "+2 Chips for each dollar you have ",
        "Diet Cola": "Sell this card to create a free Double Tag",
        "Trading Card": "If first discard of round has only 1 card, destroy it and earn $3",
        "Flash Card": "This Joker gains +2 Mult per reroll in the shop",
        "Popcorn": "+20 Mult -4 Mult per round played",
        "Ramen": "X2 Mult, loses X0.01 Mult per card discarded",
        "Seltzer": "Retrigger all cards played for the next 10 hands",
        "Spare Trousers": "Gain +2 Mult if played hand contains a Two Pair",
        "Campfire": "This Joker gains X0.25 Mult for each card sold, resets when Boss Blind is defeated",
        "Smiley Face": "Played face cards give +5 Mult when scored",
        "Ancient Joker": "Each played card with Heart suit gives X1.5 Mult when scored suit changes at end of round",
        "Walkie Talkie": "Each played 10 or 4 gives +10 Chips and +4 Mult when scored",
        "Castle": "This Joker gains +3 Chips per discarded Heart card, suit changes every round",
    }
)

scoring_rules = """
# Scoring Rules for Balatro
## 🔢 Basic Formula

The total score of a hand is calculated using the formula:

**Score = Chips × Multiplier**

This value is computed through four main stages, in the following order:

### 1. Base Hand Chip/Multiplier
- Determined by your poker hand type (e.g., Pair, Straight, Full House) and its level (upgraded via Planet cards).
- This stage adds base chips and base mult based on the hand type and level.
- Certain jokers (e.g., Space Joker) or boss effects (e.g., The Arm, The Flint) can modify hand level or base values.
- Hand type recognition can be modified by jokers like Four Fingers, Shortcut, and Smeared Joker.
- Order of cards does not affect hand recognition.

### 2. Played Cards’ Scoring
- Only scored cards (those contributing to the hand type) add chip value and trigger enhancements/effects.
- Cards are evaluated left to right, and order can influence outcomes when involving:
    - Mult-on-score effects (from jokers or “Mult” enhancement)
    - Glass cards (double next multiplier)
    - Certain jokers (e.g., Bloodstone)
- Jokers like Splash allow all played cards to be scored.
- Cards can be debuffed (e.g., by “The Verdant”) and thus won’t trigger effects or give chips.

### 3. Held-in-Hand Effects
- Applies to cards in your hand, scored or not.
- Effects include:
    - Steel-enhanced cards (×1.5 mult)
    - Baron joker (mult from Kings)
    - Shoot the Moon (mult from Queens)
    - Reserved Parking ($ chance from face cards)
    - Raised Fist (mult from lowest-ranked card)
- Red Seals trigger these effects twice.
- “The Hook” discards your hand before evaluation, disabling held effects.
- Debuffed cards do not trigger held effects.

### 4. Joker Effects
- Evaluated left to right.
- Jokers give +chips, +mult, or ×mult, based on their conditions.
- Effects can be modified by Joker enhancements:
    - Foil: +50 chips
    - Holographic: +10 mult
    - Polychrome: ×1.5 mult
- Order matters when:
    - Using Blueprint/Brainstorm
    - Combining +mult and ×mult jokers (always put ×mult to the right for maximum effect)
- Upgradeable jokers trigger upgrades before giving effect.
- Degrading jokers (e.g., Ice Cream) apply effect before degrading.
"""

shop_strategy = """
## Key Strategies for the Shop
*Prioritize Synergy*: Look for Jokers that work well together. For example, a Joker that boosts chips based on discards is excellent for a discard-heavy build. A Joker that boosts multipliers based on hand type is great if you're focusing on a specific hand like straights or flushes.
*Balance Jokers*: Aim for a mix of Jokers that provide chip boosts, multiplier boosts, and multiplier scaling (xMult). A deck with only one type of Joker can be less effective in the long run.
*Consider Hand Types*: Choose a hand type (e.g., flush, full house) and build your deck around it. This allows for more focused strategy and easier scaling with Planet and Tarot cards.
*Don't Overlook Vouchers*: Vouchers provide permanent upgrades, so keep an eye out for them in the shop after defeating bosses. Some vouchers offer significant discounts, so plan your purchases accordingly.
*Be Mindful of Blinds*: Check the upcoming blinds, especially boss blinds, to anticipate their abilities and adjust your deck accordingly.
*Reroll Strategically*: Don't be afraid to reroll the shop, especially if you have a good amount of gold and a specific Joker in mind. Rerolls become more expensive with each use, but reset after each round.
*Utilize Tarot Cards*: Tarot cards can be powerful tools for deck manipulation, allowing you to add, remove, or modify cards. They can be crucial for tailoring your deck to your chosen strategy.
*Consider Skipping Blinds*: If you can afford to skip a blind, you can potentially save money for the next shop visit and earn more interest on your gold, which can be used for future upgrades.
*Economy Matters*: Keep an eye on your gold and try to maximize interest by saving. This will allow you to purchase more upgrades in the shop.
"""
