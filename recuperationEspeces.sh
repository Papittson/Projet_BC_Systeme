
champs=$(ls Especes)
for champ in $champs
do
    echo importation de $champ
    curl -G "https://fr.wikipedia.org/w/index.php" --data-urlencode "title=${champ}" --data-urlencode "action=raw" > test/$champ
done