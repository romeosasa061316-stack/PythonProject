<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>5 Star Bible ⭐</title>

    <style>
        body {
            font-family: Arial;
            text-align: center;
            background: black;
            color: white;
        }

        h1 {
            color: gold;
        }

        .container {
            margin-top: 50px;
        }

        button {
            padding: 10px;
            margin: 10px;
            border: none;
            background: gold;
            cursor: pointer;
            border-radius: 5px;
        }

        button:hover {
            background: orange;
        }

        #result {
            margin-top: 20px;
            font-size: 18px;
        }
    </style>
</head>

<body>

    <h1>5 Star Bible ⭐</h1>

    <div class="container">
        <h3>How are you feeling today?</h3>

        <!-- Mood Buttons -->
        <button onclick="showVerse('sad')">Sad 😔</button>
        <button onclick="showVerse('happy')">Happy 😊</button>
        <button onclick="showVerse('anxious')">Anxious 😟</button>

        <!-- Output -->
        <div id="result"></div>
    </div>

    <script>
        // Mood → Verse data (dictionary)
        const verses = {
            sad: "Psalm 34:18 - The Lord is close to the brokenhearted.",
            happy: "Psalm 118:24 - This is the day the Lord has made.",
            anxious: "Philippians 4:6 - Do not be anxious about anything."
        };

        // Function
        function showVerse(mood) {

            // Get verse
            let verse = verses[mood];

            // Show verse
            document.getElementById("result").innerText = verse;
        }
    </script>

</body>
</html>