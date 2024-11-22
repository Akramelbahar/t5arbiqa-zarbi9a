from flask import Flask, render_template, request
import random
import json
app = Flask(__name__)


books = {
    "islam": [
        {
            "title": "No God but God: The Origins, Evolution and Future of Islam (Kindle Edition)",
            "author": "Reza Aslan",
            "desc": "avg rating 4.13 \u2014 27,583 ratings\u2014 published 2005",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1528328757l/40411388._SY75_.jpg"
        },
        {
            "title": "Muhammad: His Life Based on the Earliest Sources (Paperback)",
            "author": "Martin Lings",
            "desc": "avg rating 4.57 \u2014 12,951 ratings\u2014 published 1983",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1391978670l/144925._SX50_.jpg"
        },
        {
            "title": "Destiny Disrupted: A History of the World Through Islamic Eyes (Kindle Edition)",
            "author": "Tamim Ansary",
            "desc": "avg rating 4.39 \u2014 10,721 ratings\u2014 published 2009",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1489839142l/34617904._SY75_.jpg"
        },
        {
            "title": "Reclaim Your Heart: Personal Insights on Breaking Free from Life's Shackles (Paperback)",
            "author": "Yasmin Mogahed",
            "desc": "avg rating 4.41 \u2014 12,503 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1355117054l/16112413._SX50_.jpg"
        },
        {
            "title": "Secrets of Divine Love: A Spiritual Journey into the Heart of Islam (Paperback)",
            "author": "A. Helwa",
            "desc": "avg rating 4.51 \u2014 6,842 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1583659465l/52207852._SX50_.jpg"
        },
        {
            "title": "Islam: A Short History (Modern Library Chronicles)",
            "author": "Karen Armstrong",
            "desc": "avg rating 4.04 \u2014 10,591 ratings\u2014 published 2000",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1403181902l/27306._SY75_.jpg"
        },
        {
            "title": "Infidel (Hardcover)",
            "author": "Ayaan Hirsi Ali",
            "desc": "avg rating 4.19 \u2014 91,011 ratings\u2014 published 2006",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388256729l/81227._SY75_.jpg"
        },
        {
            "title": "In the Footsteps of the Prophet: Lessons from the Life of Muhammad (Hardcover)",
            "author": "Tariq Ramadan",
            "desc": "avg rating 4.45 \u2014 4,305 ratings\u2014 published 2007",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1387739361l/169338._SY75_.jpg"
        },
        {
            "title": "Purification of the Heart: Signs, Symptoms and Cures of the Spiritual Diseases of the Heart (Paperback)",
            "author": "Hamza Yusuf",
            "desc": "(Translation & Commentary)",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1430916976l/272724._SY75_.jpg"
        },
        {
            "title": "After the Prophet: The Epic Story of the Shia-Sunni Split in Islam (Hardcover)",
            "author": "Lesley Hazleton",
            "desc": "avg rating 4.09 \u2014 9,128 ratings\u2014 published 2009",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1320463957l/6533039._SY75_.jpg"
        },
        {
            "title": "\u0644\u0627 \u062a\u062d\u0632\u0646 (Paperback)",
            "author": "\u0639\u0627\u0626\u0636 \u0627\u0644\u0642\u0631\u0646\u064a",
            "desc": "avg rating 4.13 \u2014 30,649 ratings\u2014 published 2003",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1202202276l/2750180._SX50_.jpg"
        },
        {
            "title": "Muhammad: A Biography of the Prophet (Paperback)",
            "author": "Karen Armstrong",
            "desc": "avg rating 4.19 \u2014 6,917 ratings\u2014 published 1991",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388355910l/27310._SY75_.jpg"
        },
        {
            "title": "Misquoting Muhammad: The Challenge and Choices of Interpreting the Prophet's Legacy (Hardcover)",
            "author": "Jonathan A.C. Brown",
            "desc": "avg rating 4.35 \u2014 1,050 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1394522989l/20578790._SY75_.jpg"
        },
        {
            "title": "Lost Islamic History: Reclaiming Muslim Civilisation from the Past (Paperback)",
            "author": "Firas Alkhateeb",
            "desc": "avg rating 4.44 \u2014 2,753 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1430183256l/20794875._SY75_.jpg"
        },
        {
            "title": "The Autobiography of Malcolm X (Mass Market Paperback)",
            "author": "Malcolm X",
            "desc": "avg rating 4.36 \u2014 274,901 ratings\u2014 published 1965",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1434682864l/92057._SY75_.jpg"
        },
        {
            "title": "A History of God: The 4000-Year Quest of Judaism, Christianity and Islam (Hardcover)",
            "author": "Karen Armstrong",
            "desc": "avg rating 3.89 \u2014 50,572 ratings\u2014 published 1993",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1386924363l/3873._SX50_.jpg"
        },
        {
            "title": "Qur'an and Woman: Rereading the Sacred Text from a Woman's Perspective (Paperback)",
            "author": "Amina Wadud",
            "desc": "avg rating 4.23 \u2014 2,272 ratings\u2014 published 1992",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348831888l/108740._SY75_.jpg"
        },
        {
            "title": "The Road to Mecca (Paperback)",
            "author": "Muhammad Asad",
            "desc": "avg rating 4.48 \u2014 5,790 ratings\u2014 published 1954",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1431869627l/362413._SY75_.jpg"
        },
        {
            "title": "\"Believing Women\" in Islam: Unreading Patriarchal Interpretations of the Qur'an (Paperback)",
            "author": "Asma Barlas",
            "desc": "avg rating 4.27 \u2014 1,373 ratings\u2014 published 2002",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348961323l/530114._SX50_.jpg"
        },
        {
            "title": "Nine Parts of Desire: The Hidden World of Islamic Women (Paperback)",
            "author": "Geraldine Brooks",
            "desc": "avg rating 4.05 \u2014 14,642 ratings\u2014 published 1994",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1403182793l/337615._SY75_.jpg"
        },
        {
            "title": "Seeking Allah, Finding Jesus: A Devout Muslim Encounters Christianity (Paperback)",
            "author": "Nabeel Qureshi",
            "desc": "avg rating 4.58 \u2014 34,969 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1386802223l/18289396._SY75_.jpg"
        },
        {
            "title": "The Study Quran: A New Translation and Commentary (Unknown Binding)",
            "author": "Seyyed Hossein Nasr",
            "desc": "(Editor-in-Chief)",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1430747014l/15820216._SX50_.jpg"
        },
        {
            "title": "The Kite Runner (Paperback)",
            "author": "Khaled Hosseini",
            "desc": "avg rating 4.35 \u2014 3,257,202 ratings\u2014 published 2003",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1579036753l/77203._SY75_.jpg"
        },
        {
            "title": "Allah Loves (Hardcover)",
            "author": "Omar Suleiman",
            "desc": "avg rating 4.75 \u2014 1,607 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1585180394l/52677475._SY75_.jpg"
        },
        {
            "title": "Timeless Seeds of Advice: The Sayings of Prophet Muhammad \ufdfa , Ibn Taymiyyah, Ibn al-Qayyim, Ibn al-Jawzi and Other Prominent Scholars in Bringing Comfort and Hope to the Soul (Kindle Edition)",
            "author": "B.B. Abdulla",
            "desc": "avg rating 4.60 \u2014 1,868 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1571156552l/52933836._SX50_SY75_.jpg"
        },
        {
            "title": "Muhammad: A Prophet for Our Time (Eminent Lives)",
            "author": "Karen Armstrong",
            "desc": "avg rating 4.09 \u2014 3,310 ratings\u2014 published 2006",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1438034627l/8489._SX50_.jpg"
        },
        {
            "title": "A Thousand Splendid Suns (Hardcover)",
            "author": "Khaled Hosseini",
            "desc": "avg rating 4.44 \u2014 1,597,920 ratings\u2014 published 2007",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1655336738l/128029._SY75_.jpg"
        },
        {
            "title": "Women and Gender in Islam (Paperback)",
            "author": "Leila Ahmed",
            "desc": "avg rating 4.10 \u2014 1,681 ratings\u2014 published 1992",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348412577l/108700._SY75_.jpg"
        },
        {
            "title": "Islam and the Destiny of Man (Paperback)",
            "author": "Charles Le Gai Eaton",
            "desc": "avg rating 4.40 \u2014 1,173 ratings\u2014 published 1985",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388628496l/79325._SY75_.jpg"
        },
        {
            "title": "\u0627\u0644\u0625\u0633\u0644\u0627\u0645 \u0628\u064a\u0646 \u0627\u0644\u0634\u0631\u0642 \u0648\u0627\u0644\u063a\u0631\u0628 (Paperback)",
            "author": "Alija Izetbegovi\u0107",
            "desc": "avg rating 4.47 \u2014 11,708 ratings\u2014 published 1980",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1515658411l/6092250._SX50_.jpg"
        },
        {
            "title": "The Ideal Muslimah: The True Islamic Personality of the Muslim Woman as Defined in the Qur\u2019an and Sunnah (Hardcover)",
            "author": "\u0645\u062d\u0645\u062f \u0639\u0644\u064a \u0627\u0644\u0647\u0627\u0634\u0645\u064a",
            "desc": "avg rating 4.33 \u2014 1,258 ratings\u2014 published 1981",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1353069207l/527149._SX50_.jpg"
        },
        {
            "title": "The Venture of Islam, Vol 1: The Classical Age of Islam (Paperback)",
            "author": "Marshall G.S. Hodgson",
            "desc": "avg rating 4.23 \u2014 499 ratings\u2014 published 1974",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348592757l/171586._SY75_.jpg"
        },
        {
            "title": "The Productive Muslim: Where Faith Meets Productivity (Paperback)",
            "author": "Mohammed Faris",
            "desc": "avg rating 4.50 \u2014 1,740 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1455549267l/29100930._SX50_.jpg"
        },
        {
            "title": "The Butterfly Mosque: A Young American Woman's Journey to Love and Islam (Hardcover)",
            "author": "G. Willow Wilson",
            "desc": "avg rating 4.06 \u2014 5,059 ratings\u2014 published 2010",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1328823953l/7620761._SY75_.jpg"
        },
        {
            "title": "The First Muslim: The Story of Muhammad (Hardcover)",
            "author": "Lesley Hazleton",
            "desc": "avg rating 3.98 \u2014 4,705 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1350922573l/15815359._SX50_.jpg"
        },
        {
            "title": "The Muqaddimah: An Introduction to History (Paperback)",
            "author": "Ibn Khaldun",
            "desc": "avg rating 4.30 \u2014 4,549 ratings\u2014 published 1377",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1504443327l/36173910._SY75_.jpg"
        },
        {
            "title": "The Heart of Islam: Enduring Values for Humanity (Paperback)",
            "author": "Seyyed Hossein Nasr",
            "desc": "avg rating 4.31 \u2014 1,871 ratings\u2014 published 2002",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1384259421l/142124._SX50_.jpg"
        },
        {
            "title": "I Am Malala: The Story of the Girl Who Stood Up for Education and Was Shot by the Taliban (Hardcover)",
            "author": "Malala Yousafzai",
            "desc": "avg rating 4.15 \u2014 592,981 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1375414895l/17851885._SY75_.jpg"
        },
        {
            "title": "The Reconstruction of Religious Thought in Islam (Paperback)",
            "author": "Muhammad Iqbal",
            "desc": "avg rating 4.28 \u2014 1,442 ratings\u2014 published 1934",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1292394123l/536452._SY75_.jpg"
        },
        {
            "title": "Revive Your Heart: Putting Life in Perspective (Hardcover)",
            "author": "Nouman Ali Khan",
            "desc": "avg rating 4.48 \u2014 2,600 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1486979868l/31945132._SY75_.jpg"
        },
        {
            "title": "In the Shadow of the Sword: The Birth of Islam and the Rise of the Global Arab Empire (Hardcover)",
            "author": "Tom Holland",
            "desc": "avg rating 3.90 \u2014 4,872 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1333578249l/12376830._SY75_.jpg"
        },
        {
            "title": "\u0643\u064a\u0645\u064a\u0627\u0621 \u0627\u0644\u0633\u0639\u0627\u062f\u0629 (Paperback)",
            "author": "Abu Hamid al-Ghazali",
            "desc": "avg rating 4.11 \u2014 2,689 ratings\u2014 published 1105",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1425986389l/8856901._SX50_.jpg"
        },
        {
            "title": "The Essential Rumi (Paperback)",
            "author": "Jalal ad-Din Muhammad ar-Rumi",
            "desc": "avg rating 4.39 \u2014 48,438 ratings\u2014 published 1273",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1391414844l/304079._SX50_.jpg"
        },
        {
            "title": "The Divine Reality: God, Islam and the Mirage of Atheism (Paperback)",
            "author": "Hamza Andreas Tzortzis",
            "desc": "avg rating 4.47 \u2014 867 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1481949275l/33401821._SY75_.jpg"
        },
        {
            "title": "Inner Dimensions of Islamic Worship (Paperback)",
            "author": "Abu Hamid al-Ghazali",
            "desc": "avg rating 4.43 \u2014 675 ratings\u2014 published 1983",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1364865190l/498833._SX50_.jpg"
        },
        {
            "title": "The Conference of the Birds (Paperback)",
            "author": "Attar of Nishapur",
            "desc": "avg rating 4.23 \u2014 7,381 ratings\u2014 published 1177",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1523531563l/35187179._SX50_.jpg"
        },
        {
            "title": "Prayers of the Pious (Hardcover)",
            "author": "Omar Suleiman",
            "desc": "avg rating 4.73 \u2014 1,009 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1552583268l/44430409._SY75_.jpg"
        },
        {
            "title": "What Went Wrong? The Clash Between Islam & Modernity in the Middle East (Paperback)",
            "author": "Bernard Lewis",
            "desc": "avg rating 3.54 \u2014 3,783 ratings\u2014 published 2001",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1407707585l/27577._SY75_.jpg"
        },
        {
            "title": "If the Oceans Were Ink: An Unlikely Friendship and a Journey to the Heart of the Quran (Paperback)",
            "author": "Carla Power",
            "desc": "avg rating 4.11 \u2014 1,961 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1423522653l/22320455._SX50_.jpg"
        },
        {
            "title": "The Book of Assistance (Paperback)",
            "author": "\u0627\u0644\u062d\u0628\u064a\u0628 \u0639\u0628\u062f \u0627\u0644\u0644\u0647 \u0628\u0646 \u0639\u0644\u0648\u064a \u0627\u0644\u062d\u062f\u0627\u062f \u0627\u0644\u062d\u0636\u0631\u0645\u064a \u0627\u0644\u0634\u0627\u0641\u0639\u064a",
            "desc": "avg rating 4.60 \u2014 786 ratings\u2014 published 1989",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1328841189l/498802._SY75_.jpg"
        }
    ],
    "christians": [
        {
            "title": "Mere Christianity (Paperback)",
            "author": "C.S. Lewis",
            "desc": "avg rating 4.36 \u2014 431,954 ratings\u2014 published 1952",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1468102872l/11138._SY75_.jpg"
        },
        {
            "title": "The Screwtape Letters (Kindle Edition)",
            "author": "C.S. Lewis",
            "desc": "avg rating 4.27 \u2014 468,920 ratings\u2014 published 1942",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1476379778l/8130077._SY75_.jpg"
        },
        {
            "title": "The Great Divorce (Paperback)",
            "author": "C.S. Lewis",
            "desc": "avg rating 4.31 \u2014 160,199 ratings\u2014 published 1946",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1435968645l/25845273._SX50_.jpg"
        },
        {
            "title": "The Shack: Where Tragedy Confronts Eternity (Kindle Edition)",
            "author": "William Paul Young",
            "desc": "avg rating 3.83 \u2014 664,221 ratings\u2014 published 2007",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1532013572l/40874325._SY75_.jpg"
        },
        {
            "title": "Crazy Love: Overwhelmed by a Relentless God (Paperback)",
            "author": "Francis Chan",
            "desc": "avg rating 4.17 \u2014 192,479 ratings\u2014 published 2008",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1328763220l/3206011._SY75_.jpg"
        },
        {
            "title": "The Lion, the Witch and the Wardrobe (Chronicles of Narnia, #1)",
            "author": "C.S. Lewis",
            "desc": "avg rating 4.24 \u2014 2,901,597 ratings\u2014 published 1950",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1353029077l/100915._SY75_.jpg"
        },
        {
            "title": "Redeeming Love (Paperback)",
            "author": "Francine Rivers",
            "desc": "avg rating 4.51 \u2014 338,460 ratings\u2014 published 1991",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1550053167l/11422._SX50_.jpg"
        },
        {
            "title": "The Case for Christ (Mass Market Paperback)",
            "author": "Lee Strobel",
            "desc": "avg rating 4.22 \u2014 139,449 ratings\u2014 published 1998",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1448776489l/73186._SY75_.jpg"
        },
        {
            "title": "The Purpose Driven Life: What on Earth Am I Here for? (Paperback)",
            "author": "Rick Warren",
            "desc": "avg rating 3.97 \u2014 279,994 ratings\u2014 published 2002",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1440111652l/56495._SY75_.jpg"
        },
        {
            "title": "The Pilgrim's Progress (Paperback)",
            "author": "John Bunyan",
            "desc": "avg rating 4.06 \u2014 146,504 ratings\u2014 published 1678",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1405982367l/29797._SY75_.jpg"
        },
        {
            "title": "The Hiding Place: The Triumphant True Story of Corrie Ten Boom (Mass Market Paperback)",
            "author": "Corrie ten Boom",
            "desc": "avg rating 4.47 \u2014 335,058 ratings\u2014 published 1971",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1320418824l/561909._SY75_.jpg"
        },
        {
            "title": "The Problem of Pain (Paperback)",
            "author": "C.S. Lewis",
            "desc": "avg rating 4.13 \u2014 66,463 ratings\u2014 published 1940",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1504348728l/13650513._SY75_.jpg"
        },
        {
            "title": "The Reason for God: Belief in an Age of Skepticism (Hardcover)",
            "author": "Timothy J. Keller",
            "desc": "avg rating 4.23 \u2014 69,783 ratings\u2014 published 2008",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388185497l/1858013._SX50_.jpg"
        },
        {
            "title": "Left Behind (Left Behind, #1)",
            "author": "Tim LaHaye",
            "desc": "avg rating 3.86 \u2014 237,915 ratings\u2014 published 1995",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1406505054l/27523._SY75_.jpg"
        },
        {
            "title": "Heaven is for Real: A Little Boy's Astounding Story of His Trip to Heaven and Back (Paperback)",
            "author": "Todd Burpo",
            "desc": "avg rating 4.03 \u2014 326,859 ratings\u2014 published 2010",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348467278l/7933292._SY75_.jpg"
        },
        {
            "title": "The Pursuit of God: The Human Thirst for the Divine (Paperback)",
            "author": "A.W. Tozer",
            "desc": "avg rating 4.39 \u2014 80,393 ratings\u2014 published 1948",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1387714034l/672493._SY75_.jpg"
        },
        {
            "title": "The Four Loves (Paperback)",
            "author": "C.S. Lewis",
            "desc": "avg rating 4.17 \u2014 61,637 ratings\u2014 published 1960",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1483646226l/29938407._SY75_.jpg"
        },
        {
            "title": "The Magician\u2019s Nephew (Chronicles of Narnia, #6)",
            "author": "C.S. Lewis",
            "desc": "avg rating 4.05 \u2014 562,292 ratings\u2014 published 1955",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1308814770l/65605._SY75_.jpg"
        },
        {
            "title": "Knowing God (Paperback)",
            "author": "J.I. Packer",
            "desc": "avg rating 4.32 \u2014 60,186 ratings\u2014 published 1973",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348545196l/139855._SX50_.jpg"
        },
        {
            "title": "A Grief Observed (Paperback)",
            "author": "C.S. Lewis",
            "desc": "avg rating 4.22 \u2014 85,180 ratings\u2014 published 1961",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1439250484l/26077627._SX50_.jpg"
        },
        {
            "title": "Gentle and Lowly: The Heart of Christ for Sinners and Sufferers (Hardcover)",
            "author": "Dane C. Ortlund",
            "desc": "avg rating 4.52 \u2014 47,538 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1571689979l/52891090._SX50_SY75_.jpg"
        },
        {
            "title": "The 5 Love Languages: The Secret to Love that Lasts (Kindle Edition)",
            "author": "Gary Chapman",
            "desc": "avg rating 4.27 \u2014 447,341 ratings\u2014 published 1990",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1432487272l/23878688._SY75_.jpg"
        },
        {
            "title": "Prince Caspian (Chronicles of Narnia, #2)",
            "author": "C.S. Lewis",
            "desc": "avg rating 3.98 \u2014 453,965 ratings\u2014 published 1951",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1308814880l/121749._SY75_.jpg"
        },
        {
            "title": "The Horse and His Boy (Chronicles of Narnia, #5)",
            "author": "C.S. Lewis",
            "desc": "avg rating 3.91 \u2014 365,904 ratings\u2014 published 1954",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1703358949l/84119._SX50_.jpg"
        },
        {
            "title": "The Voyage of the Dawn Treader (Chronicles of Narnia, #3)",
            "author": "C.S. Lewis",
            "desc": "avg rating 4.09 \u2014 482,508 ratings\u2014 published 1952",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1661032500l/140225._SX50_.jpg"
        },
        {
            "title": "Radical: Taking Back Your Faith from the American Dream (Paperback)",
            "author": "David Platt",
            "desc": "avg rating 4.18 \u2014 65,872 ratings\u2014 published 2010",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1333580811l/7497897._SY75_.jpg"
        },
        {
            "title": "Blue Like Jazz: Nonreligious Thoughts on Christian Spirituality (Paperback)",
            "author": "Donald Miller",
            "desc": "avg rating 3.91 \u2014 116,087 ratings\u2014 published 2003",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1531261584l/7214._SY75_.jpg"
        },
        {
            "title": "The Cost of Discipleship (Paperback)",
            "author": "Dietrich Bonhoeffer",
            "desc": "avg rating 4.30 \u2014 46,445 ratings\u2014 published 1937",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348281510l/174834._SY75_.jpg"
        },
        {
            "title": "The Silver Chair (Chronicles of Narnia, #4)",
            "author": "C.S. Lewis",
            "desc": "avg rating 3.96 \u2014 309,454 ratings\u2014 published 1953",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1661032839l/65641._SY75_.jpg"
        },
        {
            "title": "The Last Battle (Chronicles of Narnia, #7)",
            "author": "C.S. Lewis",
            "desc": "avg rating 4.01 \u2014 286,311 ratings\u2014 published 1956",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1308814830l/84369._SY75_.jpg"
        },
        {
            "title": "Love Does: Discover a Secretly Incredible Life in an Ordinary World (Paperback)",
            "author": "Bob Goff",
            "desc": "avg rating 4.31 \u2014 93,660 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1335237698l/13497505._SY75_.jpg"
        },
        {
            "title": "The Ruthless Elimination of Hurry: How to Stay Emotionally Healthy and Spiritually Alive in the Chaos of the Modern World (Hardcover)",
            "author": "John Mark Comer",
            "desc": "avg rating 4.52 \u2014 68,670 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1550193763l/43982455._SY75_.jpg"
        },
        {
            "title": "The Meaning of Marriage: Facing the Complexities of Commitment with the Wisdom of God (Hardcover)",
            "author": "Timothy J. Keller",
            "desc": "avg rating 4.49 \u2014 43,068 ratings\u2014 published 2011",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1347735080l/11389341._SY75_.jpg"
        },
        {
            "title": "A Voice in the Wind (Mark of the Lion, #1)",
            "author": "Francine Rivers",
            "desc": "avg rating 4.57 \u2014 98,842 ratings\u2014 published 1993",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1459567327l/95617._SX50_.jpg"
        },
        {
            "title": "This Present Darkness (Darkness, #1)",
            "author": "Frank E. Peretti",
            "desc": "avg rating 4.24 \u2014 109,929 ratings\u2014 published 1986",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388202265l/17309._SY75_.jpg"
        },
        {
            "title": "Surprised by Joy: The Shape of My Early Life (Paperback)",
            "author": "C.S. Lewis",
            "desc": "avg rating 4.06 \u2014 65,064 ratings\u2014 published 1955",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1381407473l/121732._SY75_.jpg"
        },
        {
            "title": "Captivating: Unveiling the Mystery of a Woman's Soul (Hardcover)",
            "author": "John Eldredge",
            "desc": "avg rating 3.93 \u2014 84,135 ratings\u2014 published 2004",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1442893930l/11413._SY75_.jpg"
        },
        {
            "title": "The Chronicles of Narnia (The Chronicles of Narnia, #1-7)",
            "author": "C.S. Lewis",
            "desc": "avg rating 4.28 \u2014 672,186 ratings\u2014 published 1956",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1661032875l/11127._SY75_.jpg"
        },
        {
            "title": "Forgotten God: Reversing Our Tragic Neglect of the Holy Spirit (Paperback)",
            "author": "Francis Chan",
            "desc": "avg rating 4.13 \u2014 51,083 ratings\u2014 published 2009",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1438720585l/6515834._SY75_.jpg"
        },
        {
            "title": "Wild at Heart: Discovering the Secret of a Man's Soul (Kindle Edition)",
            "author": "John Eldredge",
            "desc": "avg rating 3.94 \u2014 83,857 ratings\u2014 published 2001",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1532094184l/40881942._SY75_.jpg"
        },
        {
            "title": "Seeking Allah, Finding Jesus: A Devout Muslim Encounters Christianity (Paperback)",
            "author": "Nabeel Qureshi",
            "desc": "avg rating 4.58 \u2014 34,969 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1386802223l/18289396._SY75_.jpg"
        },
        {
            "title": "The Prodigal God: Recovering the Heart of the Christian Faith (Hardcover)",
            "author": "Timothy J. Keller",
            "desc": "avg rating 4.42 \u2014 42,736 ratings\u2014 published 2008",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1427212055l/3116205._SX50_.jpg"
        },
        {
            "title": "Confessions (Paperback)",
            "author": "Augustine of Hippo",
            "desc": "avg rating 3.98 \u2014 66,716 ratings\u2014 published 378",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1266454051l/27037._SY75_.jpg"
        },
        {
            "title": "My Utmost for His Highest (Paperback)",
            "author": "Oswald Chambers",
            "desc": "avg rating 4.38 \u2014 81,390 ratings\u2014 published 1926",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1389470852l/175510._SY75_.jpg"
        },
        {
            "title": "The Practice of the Presence of God (Paperback)",
            "author": "Brother Lawrence",
            "desc": "avg rating 4.32 \u2014 51,978 ratings\u2014 published 1692",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1347467147l/498641._SY75_.jpg"
        },
        {
            "title": "The Abolition of Man (Paperback)",
            "author": "C.S. Lewis",
            "desc": "avg rating 4.11 \u2014 36,290 ratings\u2014 published 1943",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1435685201l/25825420._SY75_.jpg"
        },
        {
            "title": "Desiring God: Meditations of a Christian Hedonist (Paperback)",
            "author": "JohnPiper",
            "desc": "avg rating 4.17 \u2014 45,445 ratings\u2014 published 1986",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1386924844l/213367._SX50_.jpg"
        },
        {
            "title": "Don't Waste Your Life (Audible Audio)",
            "author": "JohnPiper",
            "desc": "avg rating 4.13 \u2014 33,827 ratings\u2014 published 2003",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1369824233l/347656._SY75_.jpg"
        },
        {
            "title": "The Holy Bible: King James Version (Hardcover)",
            "author": "Anonymous",
            "desc": "avg rating 4.44 \u2014 298,516 ratings\u2014 published 1611",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1631816305l/1923820._SY75_.jpg"
        },
        {
            "title": "The Weight of Glory (Paperback)",
            "author": "C.S. Lewis",
            "desc": "avg rating 4.38 \u2014 23,929 ratings\u2014 published 1949",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1460733381l/29921671._SY75_.jpg"
        }
    ],
    "jeff": [
        {
            "title": "Night(The Night Trilogy, #1)",
            "author": "Elie Wiesel",
            "desc": "avg rating 4.38 \u2014 1,282,953 ratings\u2014 published 1956",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1709507006l/1617._SY75_.jpg"
        },
        {
            "title": "The Diary of a Young Girl (Mass Market Paperback)",
            "author": "Anne Frank",
            "desc": "avg rating 4.19 \u2014 3,878,648 ratings\u2014 published 1947",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1560816565l/48855._SY75_.jpg"
        },
        {
            "title": "The Chosen (Reuven Malther, #1)",
            "author": "Chaim Potok",
            "desc": "avg rating 4.07 \u2014 94,855 ratings\u2014 published 1966",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1403191327l/187181._SY75_.jpg"
        },
        {
            "title": "The Yiddish Policemen's Union (Hardcover)",
            "author": "Michael Chabon",
            "desc": "avg rating 3.71 \u2014 78,179 ratings\u2014 published 2007",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1528196883l/16703._SX50_.jpg"
        },
        {
            "title": "My Name Is Asher Lev (Paperback)",
            "author": "Chaim Potok",
            "desc": "avg rating 4.24 \u2014 42,177 ratings\u2014 published 1972",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1385056726l/11507._SY75_.jpg"
        },
        {
            "title": "The Amazing Adventures of Kavalier & Clay (Paperback)",
            "author": "Michael Chabon",
            "desc": "avg rating 4.18 \u2014 206,309 ratings\u2014 published 2000",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1503806495l/3985._SY75_.jpg"
        },
        {
            "title": "People of the Book (Hardcover)",
            "author": "Geraldine Brooks",
            "desc": "avg rating 4.03 \u2014 149,882 ratings\u2014 published 2008",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1442955497l/1379961._SY75_.jpg"
        },
        {
            "title": "People Love Dead Jews: Reports from a Haunted Present (Hardcover)",
            "author": "Dara Horn",
            "desc": "avg rating 4.36 \u2014 9,532 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1625851271l/56769532._SY75_.jpg"
        },
        {
            "title": "The Book Thief (Kindle Edition)",
            "author": "Markus Zusak",
            "desc": "avg rating 4.39 \u2014 2,669,702 ratings\u2014 published 2005",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1522157426l/19063._SY75_.jpg"
        },
        {
            "title": "The Red Tent (Hardcover)",
            "author": "Anita Diamant",
            "desc": "avg rating 4.20 \u2014 610,810 ratings\u2014 published 1997",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1405739117l/4989._SY75_.jpg"
        },
        {
            "title": "Maus I: A Survivor's Tale: My Father Bleeds History (Maus, #1)",
            "author": "Art Spiegelman",
            "desc": "avg rating 4.38 \u2014 346,703 ratings\u2014 published 1986",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1633636988l/15196._SX50_.jpg"
        },
        {
            "title": "The Golem and the Jinni (The Golem and the Jinni, #1)",
            "author": "Helene Wecker",
            "desc": "avg rating 4.13 \u2014 126,863 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1349205573l/15819028._SX50_.jpg"
        },
        {
            "title": "Everything is Illuminated (Paperback)",
            "author": "Jonathan Safran Foer",
            "desc": "avg rating 3.89 \u2014 181,484 ratings\u2014 published 2002",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1479774440l/256566._SY75_.jpg"
        },
        {
            "title": "Number the Stars (Mass Market Paperback)",
            "author": "Lois Lowry",
            "desc": "avg rating 4.19 \u2014 585,302 ratings\u2014 published 1989",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1630542426l/47281._SX50_.jpg"
        },
        {
            "title": "Unorthodox: The Scandalous Rejection of My Hasidic Roots (Paperback)",
            "author": "Deborah Feldman",
            "desc": "avg rating 3.99 \u2014 65,276 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1336676500l/13547241._SY75_.jpg"
        },
        {
            "title": "The Complete Maus (Paperback)",
            "author": "Art Spiegelman",
            "desc": "avg rating 4.58 \u2014 231,660 ratings\u2014 published 1980",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327354180l/15195._SX50_.jpg"
        },
        {
            "title": "Man\u2019s Search for Meaning (Paperback)",
            "author": "Viktor E. Frankl",
            "desc": "avg rating 4.37 \u2014 764,344 ratings\u2014 published 1946",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1535419394l/4069._SY75_.jpg"
        },
        {
            "title": "The Weight of Ink (Kindle Edition)",
            "author": "Rachel Kadish",
            "desc": "avg rating 4.14 \u2014 38,386 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1589545927l/34471004._SY75_.jpg"
        },
        {
            "title": "The Sabbath: Its Meaning for Modern Man (Paperback)",
            "author": "Abraham Joshua Heschel",
            "desc": "avg rating 4.37 \u2014 6,860 ratings\u2014 published 1951",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1417605510l/345500._SY75_.jpg"
        },
        {
            "title": "Maus: A Survivor's Tale II: And Here My Troubles Began (Paperback)",
            "author": "Art Spiegelman",
            "desc": "avg rating 4.42 \u2014 152,012 ratings\u2014 published 1991",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1615818399l/15197._SX50_.jpg"
        },
        {
            "title": "The Heaven & Earth Grocery Store (Hardcover)",
            "author": "James McBride",
            "desc": "avg rating 3.97 \u2014 233,275 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1685350945l/65678550._SY75_.jpg"
        },
        {
            "title": "The Plot Against America (Paperback)",
            "author": "Philip Roth",
            "desc": "avg rating 3.81 \u2014 63,978 ratings\u2014 published 2004",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1553896240l/703._SY75_.jpg"
        },
        {
            "title": "Portnoy\u2019s Complaint (Paperback)",
            "author": "Philip Roth",
            "desc": "avg rating 3.70 \u2014 70,182 ratings\u2014 published 1969",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1663597516l/43945._SY75_.jpg"
        },
        {
            "title": "Spinning Silver (Kindle Edition)",
            "author": "Naomi Novik",
            "desc": "avg rating 4.19 \u2014 136,909 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1513872748l/36896898._SX50_.jpg"
        },
        {
            "title": "The Dovekeepers (Hardcover)",
            "author": "Alice Hoffman",
            "desc": "avg rating 4.06 \u2014 78,073 ratings\u2014 published 2011",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1306253903l/10950924._SY75_.jpg"
        },
        {
            "title": "The Tattooist of Auschwitz (The Tattooist of Auschwitz, #1)",
            "author": "Heather Morris",
            "desc": "avg rating 4.31 \u2014 1,030,295 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1525962117l/38359036._SY75_.jpg"
        },
        {
            "title": "The Promise (Reuven Malther, #2)",
            "author": "Chaim Potok",
            "desc": "avg rating 4.19 \u2014 13,857 ratings\u2014 published 1969",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388279694l/11499._SY75_.jpg"
        },
        {
            "title": "The History of Love (Paperback)",
            "author": "Nicole Krauss",
            "desc": "avg rating 3.92 \u2014 137,609 ratings\u2014 published 2005",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327911009l/3867._SY75_.jpg"
        },
        {
            "title": "When the Angels Left the Old Country (Hardcover)",
            "author": "Sacha Lamb",
            "desc": "avg rating 4.27 \u2014 3,261 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1650848866l/60420448._SY75_.jpg"
        },
        {
            "title": "Sarah's Key (Hardcover)",
            "author": "Tatiana de Rosnay",
            "desc": "avg rating 4.18 \u2014 482,263 ratings\u2014 published 2006",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1438863728l/556602._SX50_.jpg"
        },
        {
            "title": "Jewish Literacy: The Most Important Things to Know About the Jewish Religion, Its People and Its History (Hardcover)",
            "author": "Joseph Telushkin",
            "desc": "avg rating 4.31 \u2014 2,382 ratings\u2014 published 1991",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1439689267l/99007._SY75_.jpg"
        },
        {
            "title": "All-of-a-Kind Family (All-of-a-Kind-Family, #1)",
            "author": "Sydney Taylor",
            "desc": "avg rating 4.24 \u2014 26,264 ratings\u2014 published 1951",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1389583949l/7926._SY75_.jpg"
        },
        {
            "title": "Exodus (Mass Market Paperback)",
            "author": "Leon Uris",
            "desc": "avg rating 4.34 \u2014 100,255 ratings\u2014 published 1958",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1568189223l/42697._SY75_.jpg"
        },
        {
            "title": "The Matzah Ball (Paperback)",
            "author": "Jean Meltzer",
            "desc": "avg rating 3.63 \u2014 19,595 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1624824298l/56383019._SX50_.jpg"
        },
        {
            "title": "The Boy in the Striped Pajamas (Hardcover)",
            "author": "John Boyne",
            "desc": "avg rating 4.16 \u2014 873,835 ratings\u2014 published 2006",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1366228171l/39999._SY75_.jpg"
        },
        {
            "title": "Jews Don't Count (Hardcover)",
            "author": "David Baddiel",
            "desc": "avg rating 4.21 \u2014 12,058 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1608039721l/52710961._SY75_.jpg"
        },
        {
            "title": "The Devil's Arithmetic (Paperback)",
            "author": "Jane Yolen",
            "desc": "avg rating 4.03 \u2014 60,517 ratings\u2014 published 1988",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1342046407l/91357._SX50_.jpg"
        },
        {
            "title": "A Tale of Love and Darkness (Paperback)",
            "author": "Amos Oz",
            "desc": "avg rating 4.23 \u2014 12,115 ratings\u2014 published 2002",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1429313277l/27574._SY75_.jpg"
        },
        {
            "title": "The Boston Girl (Hardcover)",
            "author": "Anita Diamant",
            "desc": "avg rating 3.83 \u2014 86,958 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1418103945l/22450859._SX50_.jpg"
        },
        {
            "title": "Disobedience (Hardcover)",
            "author": "Naomi Alderman",
            "desc": "avg rating 3.69 \u2014 12,755 ratings\u2014 published 2006",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1438168317l/202677._SY75_.jpg"
        },
        {
            "title": "The World to Come (Paperback)",
            "author": "Dara Horn",
            "desc": "avg rating 3.87 \u2014 8,779 ratings\u2014 published 2006",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1331324069l/92644._SX50_.jpg"
        },
        {
            "title": "Survival in Auschwitz (Paperback)",
            "author": "Primo Levi",
            "desc": "avg rating 4.33 \u2014 78,794 ratings\u2014 published 1947",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1414374949l/6174._SX50_.jpg"
        },
        {
            "title": "Milk Fed (Hardcover)",
            "author": "Melissa Broder",
            "desc": "avg rating 3.57 \u2014 66,385 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1610290064l/54304105._SY75_.jpg"
        },
        {
            "title": "The Fixer (Paperback)",
            "author": "Bernard Malamud",
            "desc": "avg rating 3.98 \u2014 11,567 ratings\u2014 published 1966",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1403040386l/3066._SY75_.jpg"
        },
        {
            "title": "How Mirka Got Her Sword (Hardcover)",
            "author": "BarryDeutsch",
            "desc": "avg rating 3.74 \u2014 7,559 ratings\u2014 published 2010",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1281636442l/3516953._SX50_.jpg"
        },
        {
            "title": "Choosing a Jewish Life: A Handbook for People Converting to Judaism and for Their Family and Friends (Paperback)",
            "author": "Anita Diamant",
            "desc": "avg rating 4.22 \u2014 2,272 ratings\u2014 published 1998",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1403188643l/75508._SY75_.jpg"
        },
        {
            "title": "Here All Along: Finding Meaning, Spirituality, and a Deeper Connection to Life-in Judaism (after Finally Choosing to Look There)",
            "author": "Sarah Hurwitz",
            "desc": "avg rating 4.43 \u2014 2,513 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1560794885l/43289179._SY75_.jpg"
        },
        {
            "title": "This Is Real and You Are Completely Unprepared: The Days of Awe as a Journey of Transformation (Hardcover)",
            "author": "Alan Lew",
            "desc": "avg rating 4.42 \u2014 1,531 ratings\u2014 published 2003",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1492445243l/1174714._SY75_.jpg"
        },
        {
            "title": "The Netanyahus (Paperback)",
            "author": "Joshua Cohen",
            "desc": "avg rating 3.80 \u2014 15,498 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1661302430l/55817233._SY75_.jpg"
        },
        {
            "title": "The Color of Water: A Black Man's Tribute to His White Mother (Paperback)",
            "author": "James McBride",
            "desc": "avg rating 4.14 \u2014 127,981 ratings\u2014 published 1995",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1401311300l/29209._SY75_.jpg"
        }
    ],
    "sans": [
        {
            "title": "The God Delusion (Hardcover)",
            "author": "Richard Dawkins",
            "desc": "avg rating 3.90 \u2014 273,162 ratings\u2014 published 2006",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1347220693l/14743._SY75_.jpg"
        },
        {
            "title": "The End of Faith: Religion, Terror, and the Future of Reason (Paperback)",
            "author": "Sam Harris",
            "desc": "avg rating 3.90 \u2014 42,159 ratings\u2014 published 2004",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1408542906l/29501._SY75_.jpg"
        },
        {
            "title": "God Is Not Great: How Religion Poisons Everything (Hardcover)",
            "author": "Christopher Hitchens",
            "desc": "avg rating 3.96 \u2014 108,438 ratings\u2014 published 2007",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1411218313l/43369._SY75_.jpg"
        },
        {
            "title": "Letter to a Christian Nation (Hardcover)",
            "author": "Sam Harris",
            "desc": "avg rating 4.00 \u2014 41,068 ratings\u2014 published 2006",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1385089375l/51299._SY75_.jpg"
        },
        {
            "title": "50 Reasons People Give for Believing in a God (Paperback)",
            "author": "Guy P. Harrison",
            "desc": "avg rating 3.98 \u2014 1,926 ratings\u2014 published 2008",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1365464043l/1073773._SY75_.jpg"
        },
        {
            "title": "Waking Up: A Guide to Spirituality Without Religion (Hardcover)",
            "author": "Sam Harris",
            "desc": "avg rating 3.91 \u2014 47,817 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1415677308l/18774981._SY75_.jpg"
        },
        {
            "title": "The Varieties of Scientific Experience: A Personal View of the Search for God (Hardcover)",
            "author": "Carl Sagan",
            "desc": "avg rating 4.29 \u2014 10,510 ratings\u2014 published 2006",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1437328606l/61661._SY75_.jpg"
        },
        {
            "title": "Beyond Good and Evil (Paperback)",
            "author": "Friedrich Nietzsche",
            "desc": "avg rating 4.03 \u2014 101,191 ratings\u2014 published 1886",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388607391l/12321._SY75_.jpg"
        },
        {
            "title": "Infidel (Hardcover)",
            "author": "Ayaan Hirsi Ali",
            "desc": "avg rating 4.19 \u2014 91,011 ratings\u2014 published 2006",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388256729l/81227._SY75_.jpg"
        },
        {
            "title": "Jesus, Interrupted: Revealing the Hidden Contradictions in the Bible & Why We Don't Know About Them (Hardcover)",
            "author": "Bart D. Ehrman",
            "desc": "avg rating 3.99 \u2014 10,343 ratings\u2014 published 2009",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348078937l/6101996._SX50_.jpg"
        },
        {
            "title": "A Universe from Nothing: Why There Is Something Rather Than Nothing (Hardcover)",
            "author": "Lawrence M. Krauss",
            "desc": "avg rating 3.94 \u2014 29,745 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1365217267l/11337189._SY75_.jpg"
        },
        {
            "title": "Why We Believe in God(s): A Concise Guide to the Science of Faith",
            "author": "J. Anderson Thomson",
            "desc": "avg rating 3.95 \u2014 1,314 ratings\u2014 published 2011",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1414559040l/10361826._SX50_.jpg"
        },
        {
            "title": "The Christian Delusion: Why Faith Fails (Paperback)",
            "author": "John W. Loftus",
            "desc": "(Editor)",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1365463067l/7059143._SY75_.jpg"
        },
        {
            "title": "The New Atheism: Taking a Stand for Science and Reason (Paperback)",
            "author": "Victor J. Stenger",
            "desc": "avg rating 3.89 \u2014 925 ratings\u2014 published 2009",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1365462928l/6814897._SY75_.jpg"
        },
        {
            "title": "God, No! Signs You May Already Be an Atheist and Other Magical Tales (Hardcover)",
            "author": "Penn Jillette",
            "desc": "avg rating 3.67 \u2014 7,743 ratings\u2014 published 2011",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327935821l/8495145._SY75_.jpg"
        },
        {
            "title": "Why I Am Not a Christian and Other Essays on Religion and Related Subjects (Paperback)",
            "author": "Bertrand Russell",
            "desc": "avg rating 4.02 \u2014 21,371 ratings\u2014 published 1957",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1347925703l/472025._SY75_.jpg"
        },
        {
            "title": "Breaking the Spell: Religion as a Natural Phenomenon (Hardcover)",
            "author": "Daniel C. Dennett",
            "desc": "avg rating 3.89 \u2014 12,663 ratings\u2014 published 2006",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1406403613l/2067._SY75_.jpg"
        },
        {
            "title": "Mortality (Hardcover)",
            "author": "Christopher Hitchens",
            "desc": "avg rating 4.12 \u2014 28,344 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1337177391l/13529055._SY75_.jpg"
        },
        {
            "title": "Why People Believe Weird Things: Pseudoscience, Superstition, and Other Confusions of Our Time (Paperback)",
            "author": "Michael Shermer",
            "desc": "avg rating 3.86 \u2014 9,870 ratings\u2014 published 1997",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1312054576l/89281._SY75_.jpg"
        },
        {
            "title": "Being Logical: A Guide to Good Thinking (Paperback)",
            "author": "D.Q. McInerny",
            "desc": "avg rating 3.75 \u2014 1,971 ratings\u2014 published 2004",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1320435335l/721564._SY75_.jpg"
        },
        {
            "title": "Outgrowing God: A Beginner\u2019s Guide to Atheism (Hardcover)",
            "author": "Richard Dawkins",
            "desc": "avg rating 4.06 \u2014 5,758 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1563755518l/43532557._SY75_.jpg"
        },
        {
            "title": "Why There Is No God: Simple Responses to 20 Common Arguments for the Existence of God (Kindle Edition)",
            "author": "Armin Navabi",
            "desc": "avg rating 3.93 \u2014 2,899 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1412848900l/23346140._SX50_.jpg"
        },
        {
            "title": "The Four Horsemen: The Conversation That Sparked an Atheist Revolution (ebook)",
            "author": "Christopher Hitchens",
            "desc": "avg rating 3.98 \u2014 4,313 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1530273628l/40668391._SY75_.jpg"
        },
        {
            "title": "Unfollow: A Journey from Hatred to Hope (Kindle Edition)",
            "author": "Megan Phelps-Roper",
            "desc": "avg rating 4.15 \u2014 17,784 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1545515857l/43314707._SY75_.jpg"
        },
        {
            "title": "W\u0105ska \u015bcie\u017cka. Dlaczego odszed\u0142em z Ko\u015bcio\u0142a (Hardcover)",
            "author": "Stanis\u0142aw Obirek",
            "desc": "avg rating 4.10 \u2014 102 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1580929848l/51006665._SY75_.jpg"
        },
        {
            "title": "\u017bony gej\u00f3w. O tym, czego nikomu si\u0119 nie zdradza (Paperback)",
            "author": "Maria Mamczur",
            "desc": "avg rating 3.08 \u2014 177 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1580549449l/50792046._SY75_.jpg"
        },
        {
            "title": "Ja nie mam duszy. Sprawa Barbary Ubryk, uwi\u0119zionej zakonnicy, kt\u00f3rej histori\u0105 \u017cy\u0142a ca\u0142a Polska (Paperback)",
            "author": "Natalia Budzy\u0144ska",
            "desc": "avg rating 3.09 \u2014 99 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1574515328l/48919412._SX50_.jpg"
        },
        {
            "title": "Making Sense (Audiobook)",
            "author": "Sam Harris",
            "desc": "avg rating 4.14 \u2014 1,923 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1572666552l/48662561._SX50_.jpg"
        },
        {
            "title": "Educated (Hardcover)",
            "author": "Tara Westover",
            "desc": "avg rating 4.47 \u2014 1,636,995 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1506026635l/35133922._SY75_.jpg"
        },
        {
            "title": "Joseph Anton: A Memoir (Hardcover)",
            "author": "Salman Rushdie",
            "desc": "avg rating 3.64 \u2014 9,133 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1345767745l/13532186._SX50_.jpg"
        },
        {
            "title": "A Devil's Chaplain: Reflections on Hope, Lies, Science, and Love (Paperback)",
            "author": "Richard Dawkins",
            "desc": "avg rating 3.98 \u2014 7,868 ratings\u2014 published 2003",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1432857937l/61536._SY75_.jpg"
        },
        {
            "title": "Them: Adventures with Extremists (Paperback)",
            "author": "Jon Ronson",
            "desc": "avg rating 3.95 \u2014 21,943 ratings\u2014 published 2001",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1400199696l/1823._SY75_.jpg"
        },
        {
            "title": "The Future of an Illusion (Paperback)",
            "author": "Sigmund Freud",
            "desc": "avg rating 3.76 \u2014 6,934 ratings\u2014 published 1927",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1359672176l/80458._SY75_.jpg"
        },
        {
            "title": "On the Genealogy of Morals (Paperback)",
            "author": "Friedrich Nietzsche",
            "desc": "avg rating 4.13 \u2014 31,110 ratings\u2014 published 1887",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1386923909l/80449._SY75_.jpg"
        },
        {
            "title": "Letters from the Earth: Uncensored Writings (Paperback)",
            "author": "Mark Twain",
            "desc": "avg rating 4.18 \u2014 9,479 ratings\u2014 published 1962",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1410132027l/37813._SY75_.jpg"
        },
        {
            "title": "The Atheist's Bible: An Illustrious Collection of Irreverent Thoughts (Hardcover)",
            "author": "Joan Konner",
            "desc": "avg rating 3.92 \u2014 1,329 ratings\u2014 published 2007",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348978462l/769787._SX50_.jpg"
        },
        {
            "title": "Troublemaker: Surviving Hollywood and Scientology (Hardcover)",
            "author": "Leah Remini",
            "desc": "avg rating 4.06 \u2014 72,750 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1491248986l/26827675._SY75_.jpg"
        },
        {
            "title": "Testament: Memoir of the Thoughts and Sentiments of Jean Meslier (Hardcover)",
            "author": "Jean Meslier",
            "desc": "avg rating 4.21 \u2014 170 ratings\u2014 published 1729",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1365463179l/6516943._SY75_.jpg"
        },
        {
            "title": "Misquoting Jesus: The Story Behind Who Changed the Bible and Why (Paperback)",
            "author": "Bart D. Ehrman",
            "desc": "avg rating 3.93 \u2014 19,071 ratings\u2014 published 2005",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1407109431l/51364._SY75_.jpg"
        },
        {
            "title": "Twilight of the Idols / The Anti-Christ (Paperback)",
            "author": "Friedrich Nietzsche",
            "desc": "avg rating 4.15 \u2014 9,194 ratings\u2014 published 1889",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348303426l/43150._SY75_.jpg"
        },
        {
            "title": "The Improbability of God (Hardcover)",
            "author": "Michael Martin",
            "desc": "(Editor)",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1365463432l/2052977._SX50_.jpg"
        },
        {
            "title": "The Girard Reader (Crossroad Herder Book)",
            "author": "Ren\u00e9 Girard",
            "desc": "avg rating 4.11 \u2014 192 ratings\u2014 published 1996",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1390022519l/257787._SY75_.jpg"
        },
        {
            "title": "On the Historicity of Jesus: Why We Might Have Reason for Doubt (Hardcover)",
            "author": "Richard C. Carrier",
            "desc": "avg rating 4.32 \u2014 591 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1401938214l/21964522._SX50_.jpg"
        },
        {
            "title": "Why Religion is Natural and Science is Not (Hardcover)",
            "author": "Robert N. McCauley",
            "desc": "avg rating 3.67 \u2014 36 ratings\u2014 published 2011",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348659413l/12828337._SY75_.jpg"
        },
        {
            "title": "Christianity Is Not Great: How Faith Fails (Paperback)",
            "author": "John W. Loftus",
            "desc": "(editor)",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1408932345l/20697567._SX50_.jpg"
        },
        {
            "title": "A Manual for Creating Atheists (Paperback)",
            "author": "Peter Boghossian",
            "desc": "avg rating 3.90 \u2014 2,219 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1414558944l/17937621._SY75_.jpg"
        },
        {
            "title": "The Outsider Test for Faith: How to Know Which Religion Is True (Paperback)",
            "author": "John W. Loftus",
            "desc": "avg rating 3.93 \u2014 113 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1359387664l/17247966._SY75_.jpg"
        },
        {
            "title": "The End of Christianity (Paperback)",
            "author": "John W. Loftus",
            "desc": "avg rating 4.12 \u2014 156 ratings\u2014 published 2011",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1365463725l/9683886._SY75_.jpg"
        },
        {
            "title": "Natural Atheism (Paperback)",
            "author": "Jack David Eller",
            "desc": "avg rating 3.91 \u2014 93 ratings\u2014 published 2004",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1387720304l/672508._SY75_.jpg"
        },
        {
            "title": "Sense and Goodness Without God: A Defense of Metaphysical Naturalism (Paperback)",
            "author": "Richard C. Carrier",
            "desc": "avg rating 4.01 \u2014 804 ratings\u2014 published 2005",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1389005344l/583658._SY75_.jpg"
        }
    ],
    "Verseau": [
        {
            "title": "Aquarius Man Secrets",
            "author": "Anna Kovach",
            "desc": "avg rating 4.28 \u2014 67 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1548744537l/43748442._SX50_.jpg"
        },
        {
            "title": "The Time Traveler\u2019s Wife (ebook)",
            "author": "Audrey Niffenegger",
            "desc": "avg rating 4.00 \u2014 1,814,265 ratings\u2014 published 2003",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1380660571l/18619684._SX50_.jpg"
        },
        {
            "title": "The Custom of the Country (Paperback)",
            "author": "Edith Wharton",
            "desc": "avg rating 4.06 \u2014 14,725 ratings\u2014 published 1913",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1675953938l/26950._SY75_.jpg"
        },
        {
            "title": "Little Fires Everywhere (Hardcover)",
            "author": "Celeste Ng",
            "desc": "avg rating 4.07 \u2014 1,227,818 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1522684533l/34273236._SY75_.jpg"
        },
        {
            "title": "Project Hail Mary (Hardcover)",
            "author": "Andy Weir",
            "desc": "avg rating 4.50 \u2014 674,894 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1597695864l/54493401._SY75_.jpg"
        },
        {
            "title": "Mrs. Dalloway (Hardcover)",
            "author": "Virginia Woolf",
            "desc": "avg rating 3.79 \u2014 321,347 ratings\u2014 published 1925",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1646148221l/14942._SY75_.jpg"
        },
        {
            "title": "When Dimple Met Rishi (Dimple and Rishi, #1)",
            "author": "Sandhya Menon",
            "desc": "avg rating 3.68 \u2014 54,523 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1475687488l/28458598._SX50_.jpg"
        },
        {
            "title": "The Origin of the Zodiac (Dover Occult)",
            "author": "Rupert Gleadow",
            "desc": "avg rating 2.80 \u2014 15 ratings\u2014 published 2001",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1328866405l/6509450._SY75_.jpg"
        },
        {
            "title": "The Anxious Generation: How the Great Rewiring of Childhood Caused an Epidemic of Mental Illness (Hardcover)",
            "author": "Jonathan Haidt",
            "desc": "avg rating 4.43 \u2014 50,707 ratings\u2014 published 2024",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1711573377l/171681821._SY75_.jpg"
        },
        {
            "title": "The Laws of Human Nature (Kindle Edition)",
            "author": "Robert Greene",
            "desc": "avg rating 4.36 \u2014 23,271 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1620206225l/39330937._SY75_.jpg"
        },
        {
            "title": "Reality Transurfing Steps I-V (Kindle Edition)",
            "author": "Vadim Zeland",
            "desc": "avg rating 4.46 \u2014 2,141 ratings\u2014 published 2006",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1439736454l/23929658._SY75_.jpg"
        },
        {
            "title": "The Man Who Fell to Earth (Paperback)",
            "author": "Walter Tevis",
            "desc": "avg rating 4.05 \u2014 14,996 ratings\u2014 published 1963",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1320467516l/396329._SY75_.jpg"
        },
        {
            "title": "Convenience Store Woman (Hardcover)",
            "author": "Sayaka Murata",
            "desc": "avg rating 3.68 \u2014 311,585 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1680105376l/36739755._SX50_.jpg"
        },
        {
            "title": "Angle of Yaw (Paperback)",
            "author": "Ben Lerner",
            "desc": "avg rating 4.12 \u2014 880 ratings\u2014 published 2006",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1328758061l/128398._SY75_.jpg"
        },
        {
            "title": "The Good Part (Paperback)",
            "author": "Sophie Cousens",
            "desc": "avg rating 4.03 \u2014 32,606 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1685352418l/112976344._SX50_.jpg"
        },
        {
            "title": "All Fours (Hardcover)",
            "author": "Miranda July",
            "desc": "avg rating 3.72 \u2014 51,022 ratings\u2014 published 2024",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1695913995l/197798168._SY75_.jpg"
        },
        {
            "title": "A Clockwork Orange (Paperback)",
            "author": "Anthony Burgess",
            "desc": "avg rating 4.00 \u2014 732,449 ratings\u2014 published 1962",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1549260060l/41817486._SX50_.jpg"
        },
        {
            "title": "The Waves (Paperback)",
            "author": "Virginia Woolf",
            "desc": "avg rating 4.15 \u2014 47,037 ratings\u2014 published 1931",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1645526068l/46114._SY75_.jpg"
        },
        {
            "title": "The Ferryman (Hardcover)",
            "author": "Justin Cronin",
            "desc": "avg rating 3.92 \u2014 34,796 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1659983263l/61282437._SY75_.jpg"
        },
        {
            "title": "The Woman in the Dunes (Paperback)",
            "author": "K\u014db\u014d Abe",
            "desc": "avg rating 3.89 \u2014 35,026 ratings\u2014 published 1962",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1361254930l/9998._SY75_.jpg"
        },
        {
            "title": "Sulwe (Hardcover)",
            "author": "Lupita Nyong'o",
            "desc": "avg rating 4.66 \u2014 10,867 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1554153712l/42785750._SX50_.jpg"
        },
        {
            "title": "The Complete Cosmicomics (Hardcover)",
            "author": "Italo Calvino",
            "desc": "avg rating 4.12 \u2014 4,312 ratings\u2014 published 1997",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327969031l/6018080._SY75_.jpg"
        },
        {
            "title": "Klara and the Sun (Hardcover)",
            "author": "Kazuo Ishiguro",
            "desc": "avg rating 3.74 \u2014 371,373 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1603206535l/54120408._SY75_.jpg"
        },
        {
            "title": "The One (Kindle Edition)",
            "author": "John Marrs",
            "desc": "avg rating 4.11 \u2014 203,489 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1612001976l/40670312._SY75_.jpg"
        },
        {
            "title": "Warcross (Warcross, #1)",
            "author": "Marie Lu",
            "desc": "avg rating 4.13 \u2014 118,087 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1533058119l/41014903._SY75_.jpg"
        },
        {
            "title": "Cosmic Queries: StarTalk's Guide to Who We Are, How We Got Here, and Where We're Going (Hardcover)",
            "author": "Neil deGrasse Tyson",
            "desc": "avg rating 4.17 \u2014 3,222 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1625235780l/54503255._SY75_.jpg"
        },
        {
            "title": "Surveys (Paperback)",
            "author": "Natasha Stagg",
            "desc": "avg rating 3.34 \u2014 529 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1456359976l/27750091._SY75_.jpg"
        },
        {
            "title": "La encomienda (Paperback)",
            "author": "Margarita Garc\u00eda Robayo",
            "desc": "avg rating 3.68 \u2014 2,048 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1655538714l/61310155._SY75_.jpg"
        },
        {
            "title": "Autisterna: om kvinnor p\u00e5 spektrat (Hardcover)",
            "author": "Clara T\u00f6rnvall",
            "desc": "avg rating 4.02 \u2014 2,483 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1631310641l/58967302._SY75_.jpg"
        },
        {
            "title": "P\u00e9talos y otras historias inc\u00f3modas (Paperback)",
            "author": "Guadalupe Nettel",
            "desc": "avg rating 3.83 \u2014 1,877 ratings\u2014 published 2008",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1393222230l/3275466._SY75_.jpg"
        },
        {
            "title": "Towelhead (Paperback)",
            "author": "Alicia Erian",
            "desc": "avg rating 3.67 \u2014 4,244 ratings\u2014 published 2005",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1422682136l/54881._SY75_.jpg"
        },
        {
            "title": "Nipponia Nippon (Paperback)",
            "author": "Kazushige Abe",
            "desc": "avg rating 3.30 \u2014 541 ratings\u2014 published 2001",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1526733380l/39970403._SY75_.jpg"
        },
        {
            "title": "Helpmeet (Paperback)",
            "author": "Naben Ruthnum",
            "desc": "avg rating 3.39 \u2014 6,940 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1644436256l/60301701._SY75_.jpg"
        },
        {
            "title": "I baffi (Paperback)",
            "author": "Emmanuel Carr\u00e8re",
            "desc": "avg rating 3.73 \u2014 13,127 ratings\u2014 published 1986",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1580745560l/50723116._SY75_.jpg"
        },
        {
            "title": "Walking Through Clear Water in a Pool Painted Black (Paperback)",
            "author": "Cookie Mueller",
            "desc": "avg rating 4.46 \u2014 3,811 ratings\u2014 published 1990",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1714692955l/302243._SY75_.jpg"
        },
        {
            "title": "Open Up (Hardcover)",
            "author": "ThomasMorris",
            "desc": "avg rating 3.74 \u2014 311 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1687495373l/63211102._SY75_.jpg"
        },
        {
            "title": "Wuthering Heights (Paperback)",
            "author": "Emily Bront\u00eb",
            "desc": "avg rating 3.89 \u2014 1,881,608 ratings\u2014 published 1847",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388212715l/6185._SY75_.jpg"
        },
        {
            "title": "The Wall (Paperback)",
            "author": "Marlen Haushofer",
            "desc": "avg rating 4.03 \u2014 21,664 ratings\u2014 published 1963",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1435260852l/586852._SY75_.jpg"
        },
        {
            "title": "Death Valley (Hardcover)",
            "author": "Melissa Broder",
            "desc": "avg rating 3.48 \u2014 20,621 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1688576192l/91239751._SY75_.jpg"
        },
        {
            "title": "An Ordinary Violence (Paperback)",
            "author": "Adriana Chartrand",
            "desc": "avg rating 3.01 \u2014 427 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1677077845l/122992994._SY75_.jpg"
        },
        {
            "title": "The Performance (Hardcover)",
            "author": "Claire Thomas",
            "desc": "avg rating 3.59 \u2014 2,239 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1596429510l/54735157._SY75_.jpg"
        },
        {
            "title": "The Shame (Paperback)",
            "author": "Makenna Goodman",
            "desc": "avg rating 3.60 \u2014 1,606 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1585151344l/48828984._SY75_.jpg"
        },
        {
            "title": "Moon of the Crusted Snow (Moon, #1)",
            "author": "Waubgeshig Rice",
            "desc": "avg rating 3.85 \u2014 32,003 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1521066996l/39082248._SY75_.jpg"
        },
        {
            "title": "They: A Sequence of Unease (Hardcover)",
            "author": "Kay Dick",
            "desc": "avg rating 3.37 \u2014 4,633 ratings\u2014 published 1977",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1573781403l/1714747._SY75_.jpg"
        },
        {
            "title": "The Dolls (Paperback)",
            "author": "Ursula Scavenius",
            "desc": "avg rating 3.19 \u2014 231 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1610215018l/56605286._SX50_.jpg"
        },
        {
            "title": "Priestdaddy (Hardcover)",
            "author": "Patricia Lockwood",
            "desc": "avg rating 3.86 \u2014 24,267 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1481223015l/31920820._SY75_.jpg"
        },
        {
            "title": "Dawn (Xenogenesis, #1)",
            "author": "Octavia E. Butler",
            "desc": "avg rating 4.15 \u2014 55,791 ratings\u2014 published 1987",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1717091024l/60929._SY75_.jpg"
        },
        {
            "title": "The Lesbiana's Guide to Catholic School (Hardcover)",
            "author": "Sonora Reyes",
            "desc": "avg rating 4.27 \u2014 25,757 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1634305789l/58842731._SY75_.jpg"
        },
        {
            "title": "Wandering Souls (Hardcover)",
            "author": "Cecile Pin",
            "desc": "avg rating 4.15 \u2014 13,484 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1716405505l/60741794._SY75_.jpg"
        },
        {
            "title": "This Other Eden (Hardcover)",
            "author": "Paul Harding",
            "desc": "avg rating 3.78 \u2014 17,336 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1665472154l/61089492._SY75_.jpg"
        },
        
    ],
    "Poissons": [
        {
            "title": "Neptune, the 12th House and Pisces: The End of Hope, the Beginning of Truth (Paperback)",
            "author": "Maurice Fernandez",
            "desc": "avg rating 3.89 \u2014 28 ratings\u2014 published 2004",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1347309882l/1791004._SX50_.jpg"
        },
        {
            "title": "A River Enchanted (Elements of Cadence, #1)",
            "author": "Rebecca Ross",
            "desc": "avg rating 4.09 \u2014 69,202 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1628605286l/58132544._SY75_.jpg"
        },
        {
            "title": "The Alchemist (Paperback)",
            "author": "Paulo Coelho",
            "desc": "avg rating 3.91 \u2014 3,221,408 ratings\u2014 published 1993",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1654371463l/18144590._SY75_.jpg"
        },
        {
            "title": "The Night Circus (Hardcover)",
            "author": "Erin Morgenstern",
            "desc": "avg rating 4.01 \u2014 1,020,792 ratings\u2014 published 2011",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1387124618l/9361589._SY75_.jpg"
        },
        {
            "title": "The Pisces (Hardcover)",
            "author": "Melissa Broder",
            "desc": "avg rating 3.30 \u2014 33,259 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1500926737l/32871394._SY75_.jpg"
        },
        {
            "title": "Fever Dream (Hardcover)",
            "author": "Samanta Schweblin",
            "desc": "avg rating 3.72 \u2014 43,309 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1471279721l/30763882._SX50_.jpg"
        },
        {
            "title": "The Soul of an Octopus: A Surprising Exploration into the Wonder of Consciousness (Hardcover)",
            "author": "Sy Montgomery",
            "desc": "avg rating 3.93 \u2014 52,920 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1425611143l/22609485._SY75_.jpg"
        },
        {
            "title": "A Thousand Pieces of You (Firebird, #1)",
            "author": "Claudia Gray",
            "desc": "avg rating 3.90 \u2014 60,005 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1400166295l/17234658._SY75_.jpg"
        },
        {
            "title": "The Dreamers (Hardcover)",
            "author": "Karen Thompson Walker",
            "desc": "avg rating 3.63 \u2014 41,780 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1533916399l/34409176._SY75_.jpg"
        },
        {
            "title": "Bluets (Paperback)",
            "author": "Maggie Nelson",
            "desc": "avg rating 4.08 \u2014 50,110 ratings\u2014 published 2009",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1354902976l/6798263._SY75_.jpg"
        },
        {
            "title": "One Hundred Years of Solitude (Mass Market Paperback)",
            "author": "Gabriel Garc\u00eda M\u00e1rquez",
            "desc": "avg rating 4.12 \u2014 1,009,542 ratings\u2014 published 1967",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327881361l/320._SX50_.jpg"
        },
        {
            "title": "What I Was Doing While You Were Breeding (Paperback)",
            "author": "Kristin Newman",
            "desc": "avg rating 3.86 \u2014 22,565 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1400881229l/18373272._SY75_.jpg"
        },
        {
            "title": "The Women (Hardcover)",
            "author": "Kristin Hannah",
            "desc": "avg rating 4.62 \u2014 810,550 ratings\u2014 published 2024",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1689788358l/127305853._SY75_.jpg"
        },
        {
            "title": "Moonflower (Hardcover)",
            "author": "Kacen Callender",
            "desc": "avg rating 4.05 \u2014 600 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1633040823l/58719138._SY75_.jpg"
        },
        {
            "title": "My Pisces Heart: A Black Immigrant's Search for Home Across Four Continents (Hardcover)",
            "author": "Jennifer Neal",
            "desc": "avg rating 3.25 \u2014 4 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1711478585l/205762627._SY75_.jpg"
        },
        {
            "title": "Life of Pi (Paperback)",
            "author": "Yann Martel",
            "desc": "avg rating 3.94 \u2014 1,669,481 ratings\u2014 published 2001",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1631251689l/4214._SY75_.jpg"
        },
        {
            "title": "The Bell Jar (Paperback)",
            "author": "Sylvia Plath",
            "desc": "avg rating 4.06 \u2014 1,047,586 ratings\u2014 published 1963",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1554582218l/6514._SY75_.jpg"
        },
        {
            "title": "The House in the Cerulean Sea (Cerulean Chronicles, #1)",
            "author": "T.J. Klune",
            "desc": "avg rating 4.39 \u2014 735,449 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1569514209l/45047384._SY75_.jpg"
        },
        {
            "title": "The Perks of Being a Wallflower (Paperback)",
            "author": "Stephen Chbosky",
            "desc": "avg rating 4.23 \u2014 1,866,010 ratings\u2014 published 1999",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1650033115l/22628._SX50_.jpg"
        },
        {
            "title": "The Fine Print (Dreamland Billionaires, #1)",
            "author": "Lauren Asher",
            "desc": "avg rating 3.83 \u2014 564,482 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1671865608l/74045390._SY75_.jpg"
        },
        {
            "title": "The Light We Lost (Hardcover)",
            "author": "Jill Santopolo",
            "desc": "avg rating 3.84 \u2014 179,818 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1493724414l/32956365._SY75_.jpg"
        },
        {
            "title": "Kingdom of the Wicked (Kingdom of the Wicked, #1)",
            "author": "Kerri Maniscalco",
            "desc": "avg rating 3.88 \u2014 311,097 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1578938260l/52735921._SX50_SY75_.jpg"
        },
        {
            "title": "Eragon (The Inheritance Cycle, #1)",
            "author": "Christopher Paolini",
            "desc": "avg rating 3.95 \u2014 1,834,278 ratings\u2014 published 2002",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1366212852l/113436._SX50_.jpg"
        },
        {
            "title": "Fourth Wing (The Empyrean, #1)",
            "author": "Rebecca Yarros",
            "desc": "avg rating 4.57 \u2014 2,169,931 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1701980900l/61431922._SY75_.jpg"
        },
        {
            "title": "Fallen (Fallen, #1)",
            "author": "Lauren Kate",
            "desc": "avg rating 3.72 \u2014 597,732 ratings\u2014 published 2009",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1440619649l/6487308._SY75_.jpg"
        },
        {
            "title": "Lessons in Chemistry (Hardcover)",
            "author": "Bonnie Garmus",
            "desc": "avg rating 4.29 \u2014 1,472,920 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1714630953l/206305528._SY75_.jpg"
        },
        {
            "title": "Bride (Kindle Edition)",
            "author": "Ali Hazelwood",
            "desc": "avg rating 4.02 \u2014 435,486 ratings\u2014 published 2024",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1730451646l/181344829._SY75_.jpg"
        },
        {
            "title": "Beautyland (Hardcover)",
            "author": "Marie-Helene Bertino",
            "desc": "avg rating 4.13 \u2014 13,103 ratings\u2014 published 2024",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1685992173l/127282939._SY75_.jpg"
        },
        {
            "title": "Looking Glass Sound (Hardcover)",
            "author": "Catriona Ward",
            "desc": "avg rating 3.48 \u2014 13,995 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1667233877l/60784412._SY75_.jpg"
        },
        {
            "title": "The Undertaking of Hart and Mercy (Hart and Mercy, #1)",
            "author": "Megan Bannen",
            "desc": "avg rating 4.08 \u2014 37,394 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1639888350l/58510253._SY75_.jpg"
        },
        {
            "title": "A Study in Drowning (A Study in Drowning, #1)",
            "author": "Ava Reid",
            "desc": "avg rating 3.77 \u2014 63,809 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1675782203l/75302266._SY75_.jpg"
        },
        {
            "title": "Self-Portrait with Nothing (Hardcover)",
            "author": "Aimee Pokwatka",
            "desc": "avg rating 3.49 \u2014 1,824 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1642102082l/59807970._SY75_.jpg"
        },
        {
            "title": "Peaces (Hardcover)",
            "author": "Helen Oyeyemi",
            "desc": "avg rating 3.25 \u2014 4,622 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1601095235l/55400124._SY75_.jpg"
        },
        {
            "title": "The Poet's House (Hardcover)",
            "author": "Jean Thompson",
            "desc": "avg rating 3.59 \u2014 1,090 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1652051057l/58328440._SY75_.jpg"
        },
        {
            "title": "Mary Jane (Hardcover)",
            "author": "Jessica Anya Blau",
            "desc": "avg rating 4.14 \u2014 94,818 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1603930047l/54870208._SY75_.jpg"
        },
        {
            "title": "A Guide to Being Born (Hardcover)",
            "author": "Ramona Ausubel",
            "desc": "avg rating 3.69 \u2014 2,233 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1372023371l/16158505._SY75_.jpg"
        },
        {
            "title": "The Magic Barrel (Paperback)",
            "author": "Bernard Malamud",
            "desc": "avg rating 3.94 \u2014 2,706 ratings\u2014 published 1950",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1420668130l/14084._SY75_.jpg"
        },
        {
            "title": "Clockwork Angel (The Infernal Devices, #1)",
            "author": "Cassandra Clare",
            "desc": "avg rating 4.31 \u2014 848,076 ratings\u2014 published 2010",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1693490271l/7171637._SY75_.jpg"
        },
        {
            "title": "Hardware: The Man in the Machine (Paperback)",
            "author": "Dwayne McDuffie",
            "desc": "avg rating 3.94 \u2014 137 ratings\u2014 published 1993",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1603303501l/7021138._SY75_.jpg"
        },
        {
            "title": "Blood Syndicate (1993-1995) #4",
            "author": "Iv\u00e1n V\u00e9lez, Jr.",
            "desc": "avg rating 3.50 \u2014 4 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1619069247l/57816804._SY75_.jpg"
        },
        {
            "title": "Blood Syndicate (1993-1995) #3",
            "author": "Dwayne McDuffie",
            "desc": "avg rating 3.67 \u2014 3 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1617862496l/57664516._SY75_.jpg"
        },
        {
            "title": "Blood Syndicate (1993-1995) #2",
            "author": "Dwayne McDuffie",
            "desc": "avg rating 4.00 \u2014 4 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1616651132l/57521327._SY75_.jpg"
        },
        {
            "title": "Blood Syndicate (1993-1995) #1",
            "author": "Dwayne McDuffie",
            "desc": "avg rating 4.10 \u2014 10 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1615453473l/57374991._SY75_.jpg"
        },
        {
            "title": "These Precious Days: Essays (Hardcover)",
            "author": "Ann Patchett",
            "desc": "avg rating 4.43 \u2014 40,828 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1621841000l/56922687._SY75_.jpg"
        },
        {
            "title": "Static Shock: Trial by Fire (Paperback)",
            "author": "Dwayne McDuffie",
            "desc": "avg rating 3.88 \u2014 108 ratings\u2014 published 2000",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1307746844l/1009286._SX50_.jpg"
        },
        {
            "title": "The Virgin Suicides (Paperback)",
            "author": "Jeffrey Eugenides",
            "desc": "avg rating 3.79 \u2014 366,426 ratings\u2014 published 1993",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1319032910l/10956._SY75_.jpg"
        },
        {
            "title": "Jane Eyre (Paperback)",
            "author": "Charlotte Bront\u00eb",
            "desc": "avg rating 4.15 \u2014 2,163,208 ratings\u2014 published 1847",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1557343311l/10210._SY75_.jpg"
        },
        {
            "title": "Heartless Hunter (The Crimson Moth, #1)",
            "author": "Kristen Ciccarelli",
            "desc": "avg rating 4.21 \u2014 140,259 ratings\u2014 published 2024",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1683734080l/127305713._SY75_.jpg"
        },
        {
            "title": "Powerless (The Powerless Trilogy, #1)",
            "author": "LaurenRoberts",
            "desc": "avg rating 4.20 \u2014 466,515 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1672676191l/75513900._SX50_.jpg"
        },
        {
            "title": "A Deadly Education (The Scholomance, #1)",
            "author": "Naomi Novik",
            "desc": "avg rating 3.96 \u2014 189,007 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1596909044l/50548197._SY75_.jpg"
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        }
    ],
    "B\u00e9lier": [
        {
            "title": "Nacida bajo el fuego de Aries (Kindle Edition)",
            "author": "Florencia Bonelli",
            "desc": "avg rating 3.82 \u2014 752 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1503785387l/36129869._SY75_.jpg"
        },
        {
            "title": "Aries Fire (Kindle Edition)",
            "author": "Elaine Edelson",
            "desc": "avg rating 3.23 \u2014 99 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1334100485l/13596836._SX50_.jpg"
        },
        {
            "title": "Constellation Chronicles: The Lost Civilization of Aries (Paperback)",
            "author": "Vincent Lowry",
            "desc": "avg rating 3.92 \u2014 65 ratings\u2014 published 2008",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348673000l/5976063._SY75_.jpg"
        },
        {
            "title": "The Poppy War (The Poppy War, #1)",
            "author": "R.F. Kuang",
            "desc": "avg rating 4.17 \u2014 317,564 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1515691735l/35068705._SY75_.jpg"
        },
        {
            "title": "White Nights (Paperback)",
            "author": "Fyodor Dostoevsky",
            "desc": "avg rating 4.07 \u2014 207,650 ratings\u2014 published 1848",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1450699039l/1772910._SX50_.jpg"
        },
        {
            "title": "Aries Man Secrets",
            "author": "Anna Kovach",
            "desc": "avg rating 4.28 \u2014 119 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1548734138l/43746866._SX50_.jpg"
        },
        {
            "title": "Aries (The Zodiac Queen, #1)",
            "author": "Gemma James",
            "desc": "avg rating 3.58 \u2014 3,778 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1569668895l/49664839._SX50_SY75_.jpg"
        },
        {
            "title": "\u00c1RIES: Vol. \u00fanico (Signos) (Portuguese Edition)",
            "author": "Ky Crossfire",
            "desc": "avg rating 3.80 \u2014 30 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1546959159l/43510346._SX50_.jpg"
        },
        {
            "title": "Ram Rebel: Aries (Aries Cursed #3; Zodiac Shifters #34)",
            "author": "Cara Wylde",
            "desc": "avg rating 4.30 \u2014 20 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1523421512l/39799761._SX50_.jpg"
        },
        {
            "title": "Ram Wild: Aries (Aries Cursed #2; Zodiac Shifters #33)",
            "author": "Decadent Kane",
            "desc": "avg rating 4.63 \u2014 38 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1517694426l/38340610._SX50_.jpg"
        },
        {
            "title": "Ram Rugged: Aries (Aries Cursed #1; Zodiac Shifters #32)",
            "author": "Melissa Snark",
            "desc": "avg rating 4.63 \u2014 67 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1516845650l/38198119._SX50_.jpg"
        },
        {
            "title": "Aries Fire (Fire and Water #2)",
            "author": "Christine Besze",
            "desc": "avg rating 4.86 \u2014 22 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1464190071l/26630078._SY75_.jpg"
        },
        {
            "title": "Aries (Paperback)",
            "author": "Lara Giesbers",
            "desc": "avg rating 4.50 \u2014 8 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1486456584l/30613135._SX50_.jpg"
        },
        {
            "title": "Nacida bajo el sol de Acuario (Paperback)",
            "author": "Florencia Bonelli",
            "desc": "avg rating 3.65 \u2014 1,107 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1438459870l/26022085._SY75_.jpg"
        },
        {
            "title": "Cancer (Zodiac Twin Flame, #5)",
            "author": "Rachel Medhurst",
            "desc": "avg rating 4.32 \u2014 40 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1451311397l/28373402._SY75_.jpg"
        },
        {
            "title": "The Origin of the Zodiac (Dover Occult)",
            "author": "Rupert Gleadow",
            "desc": "avg rating 2.80 \u2014 15 ratings\u2014 published 2001",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1328866405l/6509450._SY75_.jpg"
        },
        {
            "title": "The Curious Case of Benjamin Button (Paperback)",
            "author": "F. Scott Fitzgerald",
            "desc": "avg rating 3.57 \u2014 72,164 ratings\u2014 published 1922",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1331235364l/747746._SY75_.jpg"
        },
        {
            "title": "The Big Book of Answers About The Aries Man : Get Your Aries Man To Chase You! (Kindle Edition)",
            "author": "Anna Kovach",
            "desc": "avg rating 3.70 \u2014 10 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1598988244l/55206190._SX50_.jpg"
        },
        {
            "title": "La felicidad conyugal (Paperback)",
            "author": "Leo Tolstoy",
            "desc": "avg rating 3.90 \u2014 7,404 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1331667815l/13540505._SY75_.jpg"
        },
        {
            "title": "The Weight of Oranges / Miner's Pond (Paperback)",
            "author": "Anne Michaels",
            "desc": "avg rating 4.21 \u2014 47 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1389297366l/261750._SY75_.jpg"
        },
        {
            "title": "Heart of Darkness (Paperback)",
            "author": "Joseph Conrad",
            "desc": "avg rating 3.43 \u2014 527,206 ratings\u2014 published 1899",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1392799983l/4900._SX50_.jpg"
        },
        {
            "title": "Bilinmeyen Bir Kad\u0131n\u0131n Mektubu (Hardcover)",
            "author": "Stefan Zweig",
            "desc": "avg rating 4.11 \u2014 55,688 ratings\u2014 published 1922",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1706941489l/25383991._SY75_.jpg"
        },
        {
            "title": "Circe (Hardcover)",
            "author": "Madeline Miller",
            "desc": "avg rating 4.23 \u2014 1,158,720 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1565909496l/35959740._SY75_.jpg"
        },
        {
            "title": "Fire in the Blood (Hardcover)",
            "author": "Ir\u00e8ne N\u00e9mirovsky",
            "desc": "avg rating 3.84 \u2014 6,048 ratings\u2014 published 2007",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1266579184l/534158._SX50_.jpg"
        },
        {
            "title": "Royal Savage (Savage & Ink, #1)",
            "author": "Victoria Ashley",
            "desc": "avg rating 4.14 \u2014 19,102 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1445575342l/27067323._SY75_.jpg"
        },
        {
            "title": "Biography of X (Hardcover)",
            "author": "Catherine Lacey",
            "desc": "avg rating 3.84 \u2014 11,946 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1661091831l/60784729._SX50_.jpg"
        },
        {
            "title": "The Fire Next Time (Paperback)",
            "author": "James Baldwin",
            "desc": "avg rating 4.55 \u2014 106,481 ratings\u2014 published 1963",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1657560861l/464260._SY75_.jpg"
        },
        {
            "title": "The Legend of Sleepy Hollow (Paperback)",
            "author": "Washington Irving",
            "desc": "avg rating 3.79 \u2014 142,736 ratings\u2014 published 1820",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348108368l/93261._SX50_.jpg"
        },
        {
            "title": "Lady Susan (Paperback)",
            "author": "Jane Austen",
            "desc": "avg rating 3.65 \u2014 47,527 ratings\u2014 published 1871",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1328864949l/91582._SY75_.jpg"
        },
        {
            "title": "The Marriage Portrait (Hardcover)",
            "author": "Maggie O'Farrell",
            "desc": "avg rating 4.01 \u2014 165,927 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1655741851l/60353768._SX50_.jpg"
        },
        {
            "title": "Antisocial: Online Extremists, Techno-Utopians, and the Hijacking of the American Conversation (Hardcover)",
            "author": "Andrew Marantz",
            "desc": "avg rating 4.21 \u2014 2,969 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1572244845l/44139381._SY75_.jpg"
        },
        {
            "title": "Dying of Whiteness: How the Politics of Racial Resentment Is Killing America's Heartland (Hardcover)",
            "author": "Jonathan M. Metzl",
            "desc": "avg rating 4.10 \u2014 6,397 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1542018964l/40697553._SY75_.jpg"
        },
        {
            "title": "La se\u00f1ora Dalloway en Bond Street (Hardcover)",
            "author": "Virginia Woolf",
            "desc": "avg rating 3.25 \u2014 52 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1701650325l/203157100._SX50_.jpg"
        },
        {
            "title": "A Court of Thorns and Roses (A Court of Thorns and Roses, #1)",
            "author": "Sarah J. Maas",
            "desc": "avg rating 4.18 \u2014 3,188,464 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1620324329l/50659467._SY75_.jpg"
        },
        {
            "title": "El fantasma de Canterville (Mass Market Paperback)",
            "author": "Oscar Wilde",
            "desc": "avg rating 3.79 \u2014 8,120 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1328836492l/514150._SY75_.jpg"
        },
        {
            "title": "Yours for the Taking (Hardcover)",
            "author": "GabrielleKorn",
            "desc": "avg rating 3.66 \u2014 2,963 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1680211580l/65213204._SY75_.jpg"
        },
        {
            "title": "My Life on the Road (Hardcover)",
            "author": "Gloria Steinem",
            "desc": "avg rating 4.07 \u2014 35,965 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1440005972l/15451058._SY75_.jpg"
        },
        {
            "title": "Orange Is the New Black (Hardcover)",
            "author": "Piper Kerman",
            "desc": "avg rating 3.72 \u2014 203,301 ratings\u2014 published 2010",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1320520714l/6314763._SY75_.jpg"
        },
        {
            "title": "The Lowland (Hardcover)",
            "author": "Jhumpa Lahiri",
            "desc": "avg rating 3.87 \u2014 94,693 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1366930267l/17262100._SX50_.jpg"
        },
        {
            "title": "The 1619 Project: A New Origin Story (Hardcover)",
            "author": "Nikole Hannah-Jones",
            "desc": "avg rating 4.62 \u2014 20,711 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1652703065l/57717410._SY75_.jpg"
        },
        {
            "title": "The Burning God (The Poppy War, #3)",
            "author": "R.F. Kuang",
            "desc": "avg rating 4.30 \u2014 108,872 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1584965579l/45857086._SY75_.jpg"
        },
        {
            "title": "High Fidelity (Paperback)",
            "author": "Nick Hornby",
            "desc": "avg rating 3.91 \u2014 206,811 ratings\u2014 published 1995",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327928082l/285092._SY75_.jpg"
        },
        {
            "title": "Light in Gaza: Writings Born of Fire (Paperback)",
            "author": "Jehad Abusalim",
            "desc": "(Editor)",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1661723486l/60746110._SY75_.jpg"
        },
        {
            "title": "The Hundred Years' War on Palestine: A History of Settler-Colonial Conquest and Resistance, 1917-2017 (Hardcover)",
            "author": "Rashid Khalidi",
            "desc": "avg rating 4.49 \u2014 21,157 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1556345491l/41812831._SY75_.jpg"
        },
        {
            "title": "Freedom Is a Constant Struggle (Paperback)",
            "author": "Angela Y. Davis",
            "desc": "avg rating 4.45 \u2014 30,031 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1447140494l/25330108._SY75_.jpg"
        },
        {
            "title": "Haunting Adeline (Cat and Mouse, #1)",
            "author": "H.D. Carlton",
            "desc": "avg rating 3.96 \u2014 617,154 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1628900532l/58763686._SX50_.jpg"
        },
        {
            "title": "Any Man (Kindle Edition)",
            "author": "Amber Tamblyn",
            "desc": "avg rating 3.85 \u2014 13,162 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1521121315l/35068781._SY75_.jpg"
        },
        {
            "title": "Confessions (Paperback)",
            "author": "Kanae Minato",
            "desc": "avg rating 3.95 \u2014 58,727 ratings\u2014 published 2008",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1401076501l/19161835._SX50_.jpg"
        },
        {
            "title": "Making a Scene (Hardcover)",
            "author": "Constance Wu",
            "desc": "avg rating 3.67 \u2014 8,864 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1657848792l/60604383._SY75_.jpg"
        },
        {
            "title": "Opinions: A Decade of Arguments, Criticism, and Minding Other People's Business (Hardcover)",
            "author": "Roxane Gay",
            "desc": "avg rating 4.00 \u2014 3,123 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1692819821l/123195171._SY75_.jpg"
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        }
    ],
    "Taureau": [
        {
            "title": "Wintering: The Power of Rest and Retreat in Difficult Times (Hardcover)",
            "author": "Katherine May",
            "desc": "avg rating 3.85 \u2014 52,920 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1726073493l/52623750._SY75_.jpg"
        },
        {
            "title": "Tiger Lily (ebook)",
            "author": "Jodi Lynn Anderson",
            "desc": "avg rating 3.96 \u2014 28,712 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1329681513l/7514925._SY75_.jpg"
        },
        {
            "title": "The Nightingale (Hardcover)",
            "author": "Kristin Hannah",
            "desc": "avg rating 4.63 \u2014 1,570,729 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1681839850l/21853621._SY75_.jpg"
        },
        {
            "title": "Woman of Light (Hardcover)",
            "author": "Kali Fajardo-Anstine",
            "desc": "avg rating 3.65 \u2014 12,902 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1639027745l/58587145._SY75_.jpg"
        },
        {
            "title": "Violeta (Paperback)",
            "author": "Isabel Allende",
            "desc": "avg rating 4.03 \u2014 91,001 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1623948647l/57933338._SY75_.jpg"
        },
        {
            "title": "The Garden of Broken Things (Hardcover)",
            "author": "Francesca Momplaisir",
            "desc": "avg rating 3.63 \u2014 299 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1628903007l/58065400._SY75_.jpg"
        },
        {
            "title": "Dele Weds Destiny (Hardcover)",
            "author": "Tomi Obaro",
            "desc": "avg rating 3.62 \u2014 2,789 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1637792823l/58985535._SX50_.jpg"
        },
        {
            "title": "You're Not Supposed to Die Tonight (Hardcover)",
            "author": "KalynnBayron",
            "desc": "avg rating 3.59 \u2014 19,919 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1674941592l/62039227._SY75_.jpg"
        },
        {
            "title": "Eat, Pray, Love (Paperback)",
            "author": "Elizabeth Gilbert",
            "desc": "avg rating 3.63 \u2014 1,779,679 ratings\u2014 published 2006",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1503066414l/19501._SY75_.jpg"
        },
        {
            "title": "Pineapple Street (Hardcover)",
            "author": "Jenny Jackson",
            "desc": "avg rating 3.56 \u2014 185,041 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1659404866l/61246258._SY75_.jpg"
        },
        {
            "title": "Legends & Lattes (Legends & Lattes, #1)",
            "author": "Travis Baldree",
            "desc": "avg rating 4.10 \u2014 240,218 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1654581271l/61242426._SY75_.jpg"
        },
        {
            "title": "The Picture of Dorian Gray (Paperback)",
            "author": "Oscar Wilde",
            "desc": "avg rating 4.13 \u2014 1,638,875 ratings\u2014 published 1890",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1546103428l/5297._SY75_.jpg"
        },
        {
            "title": "The Surprising Power of a Good Dumpling (Paperback)",
            "author": "Wai Chim",
            "desc": "avg rating 4.01 \u2014 4,020 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1553909568l/41197399._SY75_.jpg"
        },
        {
            "title": "The Flatshare (Hardcover)",
            "author": "Beth O'Leary",
            "desc": "avg rating 4.00 \u2014 414,804 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1552471375l/36478784._SY75_.jpg"
        },
        {
            "title": "Taurus Man Secrets: A Beginner's Guide To A Taurus Man's Heart: Tame Your Taurus (Kindle Edition)",
            "author": "Anna Kovach",
            "desc": "avg rating 4.27 \u2014 165 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1517010856l/38213381._SY75_.jpg"
        },
        {
            "title": "The Luminaries (Hardcover)",
            "author": "Eleanor Catton",
            "desc": "avg rating 3.75 \u2014 82,616 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1410524246l/17333230._SY75_.jpg"
        },
        {
            "title": "Locke & Key, Vol. 2: Head Games (Kindle Edition)",
            "author": "Joe Hill",
            "desc": "avg rating 4.31 \u2014 46,088 ratings\u2014 published 2009",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1384803670l/18652490._SY75_.jpg"
        },
        {
            "title": "Tiny Moons: A Year of Eating in Shanghai (Paperback)",
            "author": "Nina Mingya Powles",
            "desc": "avg rating 4.22 \u2014 2,185 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1579890296l/50644618._SY75_.jpg"
        },
        {
            "title": "Locke & Key, Vol. 1: Welcome to Lovecraft (Hardcover)",
            "author": "Joe Hill",
            "desc": "avg rating 4.15 \u2014 97,874 ratings\u2014 published 2008",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1377304780l/3217221._SY75_.jpg"
        },
        {
            "title": "The Fifth Wound (Paperback)",
            "author": "Aurora Mattia",
            "desc": "avg rating 4.40 \u2014 243 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1651503524l/60990853._SY75_.jpg"
        },
        {
            "title": "Tell Me I'm An Artist (Hardcover)",
            "author": "Chelsea Martin",
            "desc": "avg rating 3.92 \u2014 1,172 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1643739502l/60199552._SY75_.jpg"
        },
        {
            "title": "The Power of Birthdays, Stars & Numbers: The Complete Personology Reference Guide: An Astrology and Numerology Book (Paperback)",
            "author": "Saffi Crawford",
            "desc": "avg rating 4.19 \u2014 886 ratings\u2014 published 1998",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388180762l/47283._SX50_.jpg"
        },
        {
            "title": "Cromorama: Come il colore ha cambiato il nostro sguardo (Paperback)",
            "author": "Riccardo Falcinelli",
            "desc": "avg rating 4.47 \u2014 1,532 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1505808761l/36266532._SY75_.jpg"
        },
        {
            "title": "Vida contemplativa: Elogio de la inactividad (Kindle Edition)",
            "author": "Byung-Chul Han",
            "desc": "avg rating 3.72 \u2014 1,419 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1670620846l/64995169._SY75_.jpg"
        },
        {
            "title": "Wandering Stars (Hardcover)",
            "author": "Tommy Orange",
            "desc": "avg rating 3.87 \u2014 22,428 ratings\u2014 published 2024",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1695837414l/174147294._SY75_.jpg"
        },
        {
            "title": "They Went Left (Hardcover)",
            "author": "Monica Hesse",
            "desc": "avg rating 4.24 \u2014 14,898 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1565616572l/52701968._SX50_SY75_.jpg"
        },
        {
            "title": "The First Sister (The First Sister Trilogy, #1)",
            "author": "Linden A. Lewis",
            "desc": "avg rating 3.86 \u2014 8,246 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1584211465l/52378525._SY75_.jpg"
        },
        {
            "title": "The Great Believers (Paperback)",
            "author": "Rebecca Makkai",
            "desc": "avg rating 4.29 \u2014 148,247 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1556229367l/45304101._SY75_.jpg"
        },
        {
            "title": "Villette (Paperback)",
            "author": "Charlotte Bront\u00eb",
            "desc": "avg rating 3.78 \u2014 75,531 ratings\u2014 published 1853",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1320412741l/31173._SY75_.jpg"
        },
        {
            "title": "Big Little Lies (Paperback)",
            "author": "Liane Moriarty",
            "desc": "avg rating 4.31 \u2014 1,044,338 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1559835163l/33516773._SY75_.jpg"
        },
        {
            "title": "The Night Circus (Hardcover)",
            "author": "Erin Morgenstern",
            "desc": "avg rating 4.01 \u2014 1,020,792 ratings\u2014 published 2011",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1387124618l/9361589._SY75_.jpg"
        },
        {
            "title": "Clockwork Angel (The Infernal Devices, #1)",
            "author": "Cassandra Clare",
            "desc": "avg rating 4.31 \u2014 848,076 ratings\u2014 published 2010",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1693490271l/7171637._SY75_.jpg"
        },
        {
            "title": "The Secret Garden (Hardcover)",
            "author": "Frances Hodgson Burnett",
            "desc": "avg rating 4.16 \u2014 1,214,708 ratings\u2014 published 1911",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327873635l/2998._SY75_.jpg"
        },
        {
            "title": "Happy Place (Hardcover)",
            "author": "Emily Henry",
            "desc": "avg rating 3.98 \u2014 1,099,035 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1660145160l/61718053._SY75_.jpg"
        },
        {
            "title": "Death of a Traitor (Hamish Macbeth, #35)",
            "author": "M.C. Beaton",
            "desc": "avg rating 3.83 \u2014 2,457 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1670270423l/61237160._SY75_.jpg"
        },
        {
            "title": "Matrix (Hardcover)",
            "author": "Lauren Groff",
            "desc": "avg rating 3.68 \u2014 61,190 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1617287438l/57185348._SY75_.jpg"
        },
        {
            "title": "So This Is Ever After (Kindle Edition)",
            "author": "F.T. Lukens",
            "desc": "avg rating 3.92 \u2014 25,896 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1624819095l/55545191._SX50_.jpg"
        },
        {
            "title": "A Rogue of One's Own (A League of Extraordinary Women, #2)",
            "author": "Evie Dunmore",
            "desc": "avg rating 4.02 \u2014 43,369 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1578931679l/49202118._SX50_.jpg"
        },
        {
            "title": "The Kamogawa Food Detectives (Kamogawa Food Detectives, #1)",
            "author": "Hisashi Kashiwai",
            "desc": "avg rating 3.69 \u2014 24,206 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1692885892l/154488299._SX50_.jpg"
        },
        {
            "title": "Eleanor Oliphant Is Completely Fine (Paperback)",
            "author": "Gail Honeyman",
            "desc": "avg rating 4.23 \u2014 1,296,755 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1557858891l/35900387._SY75_.jpg"
        },
        {
            "title": "Pride and Prejudice (Paperback)",
            "author": "Jane Austen",
            "desc": "avg rating 4.29 \u2014 4,409,300 ratings\u2014 published 1813",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1320399351l/1885._SY75_.jpg"
        },
        {
            "title": "Sense and Sensibility (Paperback)",
            "author": "Jane Austen",
            "desc": "avg rating 4.09 \u2014 1,229,499 ratings\u2014 published 1811",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1397245675l/14935._SY75_.jpg"
        },
        {
            "title": "Carrie Soto Is Back (Hardcover)",
            "author": "Taylor Jenkins Reid",
            "desc": "avg rating 4.21 \u2014 590,608 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1649848581l/60435878._SY75_.jpg"
        },
        {
            "title": "All Rhodes Lead Here (Kindle Edition)",
            "author": "Mariana Zapata",
            "desc": "avg rating 4.25 \u2014 136,111 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1617355542l/57605091._SY75_.jpg"
        },
        {
            "title": "Xaviera's Supersex (Mass Market Paperback)",
            "author": "Xaviera Hollander",
            "desc": "avg rating 3.74 \u2014 66 ratings\u2014 published 1978",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1300188709l/325935._SY75_.jpg"
        },
        {
            "title": "A History of Western Philosophy (Paperback)",
            "author": "Bertrand Russell",
            "desc": "avg rating 4.13 \u2014 39,971 ratings\u2014 published 1945",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1709106488l/243685._SY75_.jpg"
        },
        {
            "title": "What Feasts at Night (Sworn Soldier, #2)",
            "author": "T. Kingfisher",
            "desc": "avg rating 3.84 \u2014 21,930 ratings\u2014 published 2024",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1683668946l/127306440._SY75_.jpg"
        },
        {
            "title": "Beautiful World, Where Are You (Paperback)",
            "author": "Sally Rooney",
            "desc": "avg rating 3.53 \u2014 427,865 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1672783505l/75555793._SY75_.jpg"
        },
        {
            "title": "His Only Weakness (Slow Burn, #6)",
            "author": "Maya Banks",
            "desc": "avg rating 3.77 \u2014 154 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1503531040l/25983186._SX50_.jpg"
        },
        {
            "title": "The Goldfinch (Hardcover)",
            "author": "Donna Tartt",
            "desc": "avg rating 3.95 \u2014 965,319 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1378710146l/17333223._SY75_.jpg"
        }
    ],
    "G\u00e9meaux": [
        {
            "title": "Dead in the Water (Gemini, #1)",
            "author": "Hailey Edwards",
            "desc": "avg rating 3.95 \u2014 4,614 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1446420255l/27409891._SX50_.jpg"
        },
        {
            "title": "The Vanishing Half (Hardcover)",
            "author": "Brit Bennett",
            "desc": "avg rating 4.14 \u2014 790,891 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1577090827l/51791252._SX50_SY75_.jpg"
        },
        {
            "title": "Head Above Water (Gemini, #2)",
            "author": "Hailey Edwards",
            "desc": "avg rating 4.13 \u2014 3,645 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1454280026l/28816542._SX50_.jpg"
        },
        {
            "title": "Gemini Man Secrets",
            "author": "Anna Kovach",
            "desc": "avg rating 4.28 \u2014 74 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1548744346l/43748412._SX50_.jpg"
        },
        {
            "title": "Hell or High Water (Gemini, #3)",
            "author": "Hailey Edwards",
            "desc": "avg rating 4.12 \u2014 2,990 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1462229323l/30077328._SX50_.jpg"
        },
        {
            "title": "Child of Darkness (Gemini, #3)",
            "author": "V.C. Andrews",
            "desc": "avg rating 3.81 \u2014 2,306 ratings\u2014 published 2005",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388438009l/397465._SY75_.jpg"
        },
        {
            "title": "Gemini (Kindle Edition)",
            "author": "Penelope Ward",
            "desc": "avg rating 3.95 \u2014 11,527 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1369603003l/17979909._SY75_.jpg"
        },
        {
            "title": "Carrying the Fire: An Astronaut's Journey (Paperback)",
            "author": "MichaelCollins",
            "desc": "avg rating 4.49 \u2014 6,102 ratings\u2014 published 1974",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1347311290l/612456._SY75_.jpg"
        },
        {
            "title": "Black Cat (Gemini, #2)",
            "author": "V.C. Andrews",
            "desc": "avg rating 3.76 \u2014 2,511 ratings\u2014 published 2004",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388438013l/226682._SY75_.jpg"
        },
        {
            "title": "Celeste (Gemini, #1)",
            "author": "V.C. Andrews",
            "desc": "avg rating 3.72 \u2014 3,634 ratings\u2014 published 2004",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1390740627l/226683._SY75_.jpg"
        },
        {
            "title": "Either/Or (Hardcover)",
            "author": "Elif Batuman",
            "desc": "avg rating 4.00 \u2014 25,276 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1637786544l/58890783._SY75_.jpg"
        },
        {
            "title": "The Unhoneymooners (Unhoneymooners, #1)",
            "author": "Christina Lauren",
            "desc": "avg rating 3.91 \u2014 954,049 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1548201335l/42201431._SY75_.jpg"
        },
        {
            "title": "Homegoing (Hardcover)",
            "author": "Yaa Gyasi",
            "desc": "avg rating 4.47 \u2014 362,691 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1448108591l/27071490._SY75_.jpg"
        },
        {
            "title": "The Collected Poems of W.B. Yeats (Paperback)",
            "author": "W.B. Yeats",
            "desc": "avg rating 4.23 \u2014 39,234 ratings\u2014 published 1933",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1436919797l/53022._SY75_.jpg"
        },
        {
            "title": "Howl and Other Poems (Hardcover)",
            "author": "Allen Ginsberg",
            "desc": "avg rating 4.13 \u2014 114,289 ratings\u2014 published 1956",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1668784961l/6295._SX50_.jpg"
        },
        {
            "title": "Tess of the D\u2019Urbervilles (Paperback)",
            "author": "Thomas Hardy",
            "desc": "avg rating 3.83 \u2014 290,599 ratings\u2014 published 1891",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1633063778l/32261._SY75_.jpg"
        },
        {
            "title": "The Chaos of Stars (Hardcover)",
            "author": "Kiersten White",
            "desc": "avg rating 3.57 \u2014 10,331 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1360570534l/12578305._SX50_.jpg"
        },
        {
            "title": "Unearthed (Unearthed, #1)",
            "author": "Amie Kaufman",
            "desc": "avg rating 3.81 \u2014 7,780 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1495338043l/25446297._SX50_.jpg"
        },
        {
            "title": "Six of Crows (Six of Crows, #1)",
            "author": "Leigh Bardugo",
            "desc": "avg rating 4.48 \u2014 1,021,951 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1651710803l/23437156._SY75_.jpg"
        },
        {
            "title": "Twinmaker (Twinmaker, #1)",
            "author": "Sean Williams",
            "desc": "avg rating 3.38 \u2014 1,372 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1361330396l/17296692._SY75_.jpg"
        },
        {
            "title": "A Tale of Two Cities (Paperback)",
            "author": "Charles Dickens",
            "desc": "avg rating 3.87 \u2014 970,144 ratings\u2014 published 1859",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1344922523l/1953._SY75_.jpg"
        },
        {
            "title": "A Wrinkle in Time (Time Quintet, #1)",
            "author": "Madeleine L'Engle",
            "desc": "avg rating 3.98 \u2014 1,229,861 ratings\u2014 published 1962",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1507963312l/33574273._SX50_.jpg"
        },
        {
            "title": "Over the Moon (Lorimar Pack, #3)",
            "author": "Hailey Edwards",
            "desc": "avg rating 4.28 \u2014 1,665 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1497472502l/35436112._SY75_.jpg"
        },
        {
            "title": "Wolf at the Door (Lorimar Pack, #2)",
            "author": "Hailey Edwards",
            "desc": "avg rating 4.16 \u2014 1,839 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1477726279l/32803941._SY75_.jpg"
        },
        {
            "title": "Promise the Moon (Lorimar Pack #1)",
            "author": "Hailey Edwards",
            "desc": "avg rating 4.13 \u2014 2,092 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1470466327l/31359308._SY75_.jpg"
        },
        {
            "title": "Project Gemini: America in Space Series (America in Space Series, 1)",
            "author": "Eugen Reichl",
            "desc": "avg rating 4.38 \u2014 16 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1450038343l/27507436._SX50_.jpg"
        },
        {
            "title": "Ulysses (Paperback)",
            "author": "James Joyce",
            "desc": "avg rating 3.76 \u2014 131,306 ratings\u2014 published 1922",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1428891345l/338798._SY75_.jpg"
        },
        {
            "title": "Jake Undone (Jake, #1)",
            "author": "Penelope Ward",
            "desc": "avg rating 4.10 \u2014 23,001 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1663707575l/62673464._SY75_.jpg"
        },
        {
            "title": "City of Laughter (Hardcover)",
            "author": "Temim Fruchter",
            "desc": "avg rating 3.75 \u2014 802 ratings\u2014 published 2024",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1687392886l/128713487._SY75_.jpg"
        },
        {
            "title": "The Sign of Four (Sherlock Holmes, #2)",
            "author": "Arthur Conan Doyle",
            "desc": "avg rating 3.89 \u2014 164,717 ratings\u2014 published 1890",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1299346921l/608474._SY75_.jpg"
        },
        {
            "title": "\u99c8\u8fbc\u307f\u8a34\u3048 [Kakekomi uttae] (Kindle Edition)",
            "author": "Osamu Dazai",
            "desc": "avg rating 4.23 \u2014 61 ratings\u2014 published 1940",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1385044404l/18877541._SY75_.jpg"
        },
        {
            "title": "Taurus Man Secrets: A Beginner's Guide To A Taurus Man's Heart: Tame Your Taurus (Kindle Edition)",
            "author": "Anna Kovach",
            "desc": "avg rating 4.27 \u2014 165 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1517010856l/38213381._SY75_.jpg"
        },
        {
            "title": "Happy Place (Hardcover)",
            "author": "Emily Henry",
            "desc": "avg rating 3.98 \u2014 1,099,035 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1660145160l/61718053._SY75_.jpg"
        },
        {
            "title": "Yellowface (Hardcover)",
            "author": "R.F. Kuang",
            "desc": "avg rating 3.76 \u2014 673,183 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1671336608l/62047984._SY75_.jpg"
        },
        {
            "title": "Everyone in This Room Will Someday Be Dead (Paperback)",
            "author": "Emily R. Austin",
            "desc": "avg rating 3.86 \u2014 70,199 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1655915331l/59366182._SY75_.jpg"
        },
        {
            "title": "All's Well (Paperback)",
            "author": "Mona Awad",
            "desc": "avg rating 3.74 \u2014 28,442 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1657125309l/59366193._SY75_.jpg"
        },
        {
            "title": "Brideshead Revisited: The Sacred and Profane Memories of Captain Charles Ryder (Paperback)",
            "author": "Evelyn Waugh",
            "desc": "avg rating 4.00 \u2014 118,621 ratings\u2014 published 1945",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1621038975l/58045504._SY75_.jpg"
        },
        {
            "title": "Worry (Hardcover)",
            "author": "AlexandraTanner",
            "desc": "avg rating 3.33 \u2014 6,056 ratings\u2014 published 2024",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1710424295l/176443441._SY75_.jpg"
        },
        {
            "title": "Human Blues (Hardcover)",
            "author": "Elisa Albert",
            "desc": "avg rating 3.27 \u2014 629 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1654704188l/59366184._SY75_.jpg"
        },
        {
            "title": "Sisters (Paperback)",
            "author": "Daisy Johnson",
            "desc": "avg rating 3.47 \u2014 15,135 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1576016526l/50788186._SX50_SY75_.jpg"
        },
        {
            "title": "Still Life with Bread Crumbs (Hardcover)",
            "author": "Anna Quindlen",
            "desc": "avg rating 3.68 \u2014 52,784 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1403168088l/17884042._SX50_.jpg"
        },
        {
            "title": "The Authenticity Project (Paperback)",
            "author": "Clare Pooley",
            "desc": "avg rating 3.94 \u2014 88,169 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1603751298l/55789067._SX50_.jpg"
        },
        {
            "title": "The Keeper of Lost Things (ebook)",
            "author": "Ruth Hogan",
            "desc": "avg rating 3.80 \u2014 155,776 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1482919773l/30363088._SX50_.jpg"
        },
        {
            "title": "\u0627\u0644\u0641\u0643\u0631 \u0627\u0644\u062c\u0630\u0631\u064a : \u0623\u0637\u0631\u0648\u062d\u0629 \u0645\u0648\u062a \u0627\u0644\u0648\u0627\u0642\u0639 (Paperback)",
            "author": "Jean Baudrillard",
            "desc": "avg rating 3.59 \u2014 70 ratings\u2014 published 2001",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1305434763l/11371152._SY75_.jpg"
        },
        {
            "title": "Liberation Day (Hardcover)",
            "author": "George Saunders",
            "desc": "avg rating 3.99 \u2014 13,750 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1679496599l/60471573._SY75_.jpg"
        },
        {
            "title": "When We Were Sisters (Hardcover)",
            "author": "Fatimah Asghar",
            "desc": "avg rating 3.93 \u2014 5,883 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1648411572l/60279775._SY75_.jpg"
        },
        {
            "title": "The Dead Romantics (Paperback)",
            "author": "Ashley Poston",
            "desc": "avg rating 3.93 \u2014 196,374 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1649027850l/58885776._SX50_.jpg"
        },
        {
            "title": "The Maid (Molly the Maid, #1)",
            "author": "Nita Prose",
            "desc": "avg rating 3.76 \u2014 610,782 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1643228739l/55196813._SY75_.jpg"
        },
        {
            "title": "The Guncle (The Guncle, #1)",
            "author": "StevenRowley",
            "desc": "avg rating 4.13 \u2014 161,629 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1594848421l/54508798._SY75_.jpg"
        },
        {
            "title": "There There (Hardcover)",
            "author": "Tommy Orange",
            "desc": "avg rating 3.98 \u2014 199,245 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1512071034l/36692478._SY75_.jpg"
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        }
    ],
    "Cancer": [
        {
            "title": "The Fault in Our Stars (Hardcover)",
            "author": "John Green",
            "desc": "avg rating 4.13 \u2014 5,339,984 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1660273739l/11870085._SX50_.jpg"
        },
        {
            "title": "The Immortal Life of Henrietta Lacks (Hardcover)",
            "author": "Rebecca Skloot",
            "desc": "avg rating 4.12 \u2014 757,927 ratings\u2014 published 2010",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327878144l/6493208._SY75_.jpg"
        },
        {
            "title": "When Breath Becomes Air (Kindle Edition)",
            "author": "Paul Kalanithi",
            "desc": "avg rating 4.40 \u2014 712,732 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1492677644l/25899336._SX50_.jpg"
        },
        {
            "title": "My Sister\u2019s Keeper (Paperback)",
            "author": "Jodi Picoult",
            "desc": "avg rating 4.10 \u2014 1,241,515 ratings\u2014 published 2004",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1369504683l/10917._SY75_.jpg"
        },
        {
            "title": "A Monster Calls (Paperback)",
            "author": "Patrick Ness",
            "desc": "avg rating 4.35 \u2014 273,906 ratings\u2014 published 2011",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1430763000l/25480342._SY75_.jpg"
        },
        {
            "title": "Me and Earl and the Dying Girl (Hardcover)",
            "author": "Jesse Andrews",
            "desc": "avg rating 3.51 \u2014 144,856 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1337216932l/12700353._SX50_.jpg"
        },
        {
            "title": "The Last Lecture (Kindle Edition)",
            "author": "Randy Pausch",
            "desc": "avg rating 4.26 \u2014 352,295 ratings\u2014 published 2008",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1529682044l/40611510._SX50_.jpg"
        },
        {
            "title": "Between Two Kingdoms: A Memoir of a Life Interrupted (Hardcover)",
            "author": "Suleika Jaouad",
            "desc": "avg rating 4.43 \u2014 102,825 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1579614170l/50743767._SY75_.jpg"
        },
        {
            "title": "Before I Die (Hardcover)",
            "author": "Jenny Downham",
            "desc": "avg rating 3.81 \u2014 56,862 ratings\u2014 published 2007",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348002855l/1314332._SX50_.jpg"
        },
        {
            "title": "The End of Your Life Book Club (Hardcover)",
            "author": "Will Schwalbe",
            "desc": "avg rating 3.81 \u2014 55,097 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1333576665l/13414676._SX50_.jpg"
        },
        {
            "title": "Drums, Girls & Dangerous Pie (Drums, Girls & Dangerous Pie #1)",
            "author": "Jordan Sonnenblick",
            "desc": "avg rating 4.24 \u2014 29,900 ratings\u2014 published 2005",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1377989934l/318404._SX50_.jpg"
        },
        {
            "title": "Crying in H Mart (Hardcover)",
            "author": "Michelle Zauner",
            "desc": "avg rating 4.26 \u2014 481,393 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1601937850l/54814676._SX50_.jpg"
        },
        {
            "title": "Anticancer. A New Way of Life (Hardcover)",
            "author": "David Servan-Schreiber",
            "desc": "avg rating 4.39 \u2014 5,503 ratings\u2014 published 2007",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1189784346l/1886829._SY75_.jpg"
        },
        {
            "title": "The Honest Truth (Hardcover)",
            "author": "Dan Gemeinhart",
            "desc": "avg rating 4.24 \u2014 13,710 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1403803946l/22571259._SY75_.jpg"
        },
        {
            "title": "Zac and Mia (Paperback)",
            "author": "A.J. Betts",
            "desc": "avg rating 3.65 \u2014 12,673 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1372227353l/15757486._SY75_.jpg"
        },
        {
            "title": "After Ever After (Hardcover)",
            "author": "Jordan Sonnenblick",
            "desc": "avg rating 4.21 \u2014 11,510 ratings\u2014 published 2010",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388210788l/6693329._SX50_.jpg"
        },
        {
            "title": "Side Effects May Vary (Kindle Edition)",
            "author": "Julie Murphy",
            "desc": "avg rating 3.41 \u2014 14,430 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1371749688l/15728577._SX50_.jpg"
        },
        {
            "title": "Stitches: A Memoir (Hardcover)",
            "author": "David Small",
            "desc": "avg rating 4.06 \u2014 27,324 ratings\u2014 published 2009",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1651672111l/6407014._SX50_.jpg"
        },
        {
            "title": "The Art of Racing in the Rain (Hardcover)",
            "author": "Garth Stein",
            "desc": "avg rating 4.23 \u2014 532,492 ratings\u2014 published 2008",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1377206302l/3153910._SY75_.jpg"
        },
        {
            "title": "Everything Happens for a Reason: And Other Lies I've Loved (Hardcover)",
            "author": "Kate Bowler",
            "desc": "avg rating 3.80 \u2014 50,160 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1504731691l/35133923._SY75_.jpg"
        },
        {
            "title": "Mortality (Hardcover)",
            "author": "Christopher Hitchens",
            "desc": "avg rating 4.12 \u2014 28,344 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1337177391l/13529055._SY75_.jpg"
        },
        {
            "title": "A Walk to Remember (Kindle Edition)",
            "author": "Nicholas Sparks",
            "desc": "avg rating 4.20 \u2014 821,808 ratings\u2014 published 1999",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1498755310l/35545737._SY75_.jpg"
        },
        {
            "title": "The Bright Hour: A Memoir of Living and Dying (Hardcover)",
            "author": "Nina Riggs",
            "desc": "avg rating 4.30 \u2014 18,416 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1507193499l/34104392._SY75_.jpg"
        },
        {
            "title": "This Star Won't Go Out: The Life and Words of Esther Grace Earl (Hardcover)",
            "author": "Esther Earl",
            "desc": "avg rating 4.14 \u2014 16,197 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1392015126l/17675031._SY75_.jpg"
        },
        {
            "title": "I'm Glad My Mom Died (ebook)",
            "author": "Jennette McCurdy",
            "desc": "avg rating 4.45 \u2014 1,173,078 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1649286799l/59364173._SY75_.jpg"
        },
        {
            "title": "Autobiography of a Face (Paperback)",
            "author": "Lucy Grealy",
            "desc": "avg rating 3.97 \u2014 29,053 ratings\u2014 published 1994",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1386921470l/534255._SY75_.jpg"
        },
        {
            "title": "In Five Years (Hardcover)",
            "author": "Rebecca Serle",
            "desc": "avg rating 3.78 \u2014 539,988 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1586399012l/50093704._SY75_.jpg"
        },
        {
            "title": "The Summer I Turned Pretty (Summer, #1)",
            "author": "Jenny Han",
            "desc": "avg rating 3.75 \u2014 879,862 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1361666855l/5821978._SY75_.jpg"
        },
        {
            "title": "Radical Remission: Surviving Cancer Against All Odds (Kindle Edition)",
            "author": "Kelly A. Turner",
            "desc": "avg rating 4.42 \u2014 2,294 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1410132751l/18053023._SY75_.jpg"
        },
        {
            "title": "The Undying (Paperback)",
            "author": "Anne Boyer",
            "desc": "avg rating 4.16 \u2014 5,051 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1573603626l/40664707._SX50_.jpg"
        },
        {
            "title": "Wink (Hardcover)",
            "author": "Rob Harrell",
            "desc": "avg rating 4.27 \u2014 6,229 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1565705561l/52516178._SY75_.jpg"
        },
        {
            "title": "Being Mortal: Medicine and What Matters in the End (Hardcover)",
            "author": "Atul Gawande",
            "desc": "avg rating 4.49 \u2014 199,907 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1408324949l/20696006._SY75_.jpg"
        },
        {
            "title": "The Unlikely Pilgrimage of Harold Fry (Harold Fry, #1)",
            "author": "Rachel Joyce",
            "desc": "avg rating 3.94 \u2014 185,564 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1335816092l/13227454._SY75_.jpg"
        },
        {
            "title": "Ways to Live Forever (Paperback)",
            "author": "Sally Nicholls",
            "desc": "avg rating 4.19 \u2014 9,220 ratings\u2014 published 2008",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348098140l/2164318._SY75_.jpg"
        },
        {
            "title": "It's Not About the Bike: My Journey Back to Life (Paperback)",
            "author": "Lance Armstrong",
            "desc": "avg rating 3.71 \u2014 40,899 ratings\u2014 published 1999",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1433639489l/2265._SY75_.jpg"
        },
        {
            "title": "Ida B. . . and Her Plans to Maximize Fun, Avoid Disaster, and (Possibly) Save the World",
            "author": "Katherine Hannigan",
            "desc": "avg rating 3.89 \u2014 23,552 ratings\u2014 published 2004",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1386924484l/207802._SX50_.jpg"
        },
        {
            "title": "The Cancer Code: A Revolutionary New Understanding of a Medical Mystery (ebook)",
            "author": "Jason Fung",
            "desc": "avg rating 4.46 \u2014 2,445 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1594616707l/52163526._SY75_.jpg"
        },
        {
            "title": "Ms. Bixby's Last Day (Hardcover)",
            "author": "John DavidAnderson",
            "desc": "avg rating 4.27 \u2014 8,847 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1457894475l/27064348._SY75_.jpg"
        },
        {
            "title": "Second Chance Summer (Hardcover)",
            "author": "Morgan Matson",
            "desc": "avg rating 4.12 \u2014 54,835 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1337189920l/11071466._SY75_.jpg"
        },
        {
            "title": "The Middle Place (Hardcover)",
            "author": "Kelly Corrigan",
            "desc": "avg rating 3.88 \u2014 32,403 ratings\u2014 published 2005",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1347969743l/1779929._SY75_.jpg"
        },
        {
            "title": "The Lemonade Club (Hardcover)",
            "author": "Patricia Polacco",
            "desc": "avg rating 4.45 \u2014 919 ratings\u2014 published 2007",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348343162l/443614._SX50_.jpg"
        },
        {
            "title": "Dancing at the Pity Party: A Dead Mom Graphic Memoir (Hardcover)",
            "author": "Tyler Feder",
            "desc": "avg rating 4.51 \u2014 10,692 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1571889853l/50010932._SX50_SY75_.jpg"
        },
        {
            "title": "Counting Thyme (Hardcover)",
            "author": "Melanie Conklin",
            "desc": "avg rating 4.27 \u2014 2,914 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1441722559l/25938399._SY75_.jpg"
        },
        {
            "title": "The Probability of Miracles (Hardcover)",
            "author": "WendyWunder",
            "desc": "avg rating 3.90 \u2014 10,119 ratings\u2014 published 2011",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1301695123l/10710505._SY75_.jpg"
        },
        {
            "title": "Firefly Lane (Firefly Lane, #1)",
            "author": "Kristin Hannah",
            "desc": "avg rating 4.18 \u2014 421,608 ratings\u2014 published 2008",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1362435448l/1472878._SY75_.jpg"
        },
        {
            "title": "Red, White, and Whole (Hardcover)",
            "author": "Rajani LaRocca",
            "desc": "avg rating 4.42 \u2014 7,321 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1601591991l/53327892._SY75_.jpg"
        },
        {
            "title": "Slammed (Slammed, #1)",
            "author": "Colleen Hoover",
            "desc": "avg rating 4.16 \u2014 404,820 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1464826448l/30333938._SY75_.jpg"
        },
        {
            "title": "MY BATTLE AGAINST CANCER: Survivor protocol : foreword by Thomas Seyfried (Kindle Edition)",
            "author": "Nathalie Loth",
            "desc": "avg rating 4.47 \u2014 146 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1642278293l/60132194._SY75_.jpg"
        },
        {
            "title": "The Cancer Journals (Paperback)",
            "author": "Audre Lorde",
            "desc": "avg rating 4.43 \u2014 4,648 ratings\u2014 published 1980",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388177679l/50682._SY75_.jpg"
        },
        {
            "title": "Maybe One Day (Hardcover)",
            "author": "Melissa Kantor",
            "desc": "avg rating 3.96 \u2014 7,744 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1380219552l/18053047._SY75_.jpg"
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        }
    ],
    "Lion": [
        {
            "title": "The Lion, the Witch and the Wardrobe (Chronicles of Narnia, #1)",
            "author": "C.S. Lewis",
            "desc": "avg rating 4.24 \u2014 2,901,609 ratings\u2014 published 1950",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1353029077l/100915._SY75_.jpg"
        },
        {
            "title": "The Lion and the Mouse (Hardcover)",
            "author": "Jerry Pinkney",
            "desc": "avg rating 4.22 \u2014 24,281 ratings\u2014 published 2009",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1259865825l/6534132._SX50_.jpg"
        },
        {
            "title": "The Wonderful Wizard of Oz (Oz, #1)",
            "author": "L. Frank Baum",
            "desc": "avg rating 4.00 \u2014 469,707 ratings\u2014 published 1900",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1398003737l/236093._SY75_.jpg"
        },
        {
            "title": "Library Lion (Hardcover)",
            "author": "Michelle Knudsen",
            "desc": "avg rating 4.43 \u2014 11,023 ratings\u2014 published 2006",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1320438765l/127179._SX50_.jpg"
        },
        {
            "title": "When an Alpha Purrs (A Lion's Pride, #1)",
            "author": "Eve Langlais",
            "desc": "avg rating 3.84 \u2014 8,234 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1434294854l/25553015._SY75_.jpg"
        },
        {
            "title": "Watch Out for the Lion! (Hardcover)",
            "author": "Brooke Hartman",
            "desc": "avg rating 4.12 \u2014 327 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1658831795l/60827480._SX50_.jpg"
        },
        {
            "title": "How to Be a Lion (Hardcover)",
            "author": "Ed Vere",
            "desc": "avg rating 4.12 \u2014 1,300 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1511123960l/36349383._SX50_.jpg"
        },
        {
            "title": "Little Red and the Very Hungry Lion (Hardcover)",
            "author": "Alex T. Smith",
            "desc": "avg rating 4.14 \u2014 1,286 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1433444043l/25664625._SX50_.jpg"
        },
        {
            "title": "Lion Lessons (Hardcover)",
            "author": "Jon Agee",
            "desc": "avg rating 3.84 \u2014 1,887 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1453059019l/27209447._SX50_.jpg"
        },
        {
            "title": "A Hungry Lion, or A Dwindling Assortment of Animals (Hardcover)",
            "author": "Lucy Ruth Cummins",
            "desc": "avg rating 4.11 \u2014 1,770 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1452817600l/25785644._SX50_.jpg"
        },
        {
            "title": "When a Beta Roars (A Lion's Pride, #2)",
            "author": "Eve Langlais",
            "desc": "avg rating 4.01 \u2014 3,923 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1431427701l/25525645._SY75_.jpg"
        },
        {
            "title": "Tempting the Beast (Breeds, #1)",
            "author": "Lora Leigh",
            "desc": "avg rating 3.91 \u2014 24,277 ratings\u2014 published 2003",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1255718976l/592806._SY75_.jpg"
        },
        {
            "title": "Sun Flower Lion (Hardcover)",
            "author": "Kevin Henkes",
            "desc": "avg rating 3.52 \u2014 621 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1586232391l/51283707._SX50_.jpg"
        },
        {
            "title": "The Lion Inside (Hardcover)",
            "author": "Rachel Bright",
            "desc": "avg rating 4.41 \u2014 3,010 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1441808718l/26257320._SX50_.jpg"
        },
        {
            "title": "He Ain't Lion (Ridgeville, #1)",
            "author": "Celia Kyle",
            "desc": "avg rating 3.80 \u2014 4,677 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1458644347l/27162009._SX50_.jpg"
        },
        {
            "title": "Disney's The Lion King (Hardcover)",
            "author": "Don Ferguson",
            "desc": "avg rating 4.51 \u2014 23,083 ratings\u2014 published 1994",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1387751618l/1693617._SX50_.jpg"
        },
        {
            "title": "The Mane Event (Pride, #1)",
            "author": "Shelly Laurenston",
            "desc": "avg rating 3.96 \u2014 26,361 ratings\u2014 published 2007",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388627011l/341027._SY75_.jpg"
        },
        {
            "title": "A Lion Called Christian: The True Story of the Remarkable Bond Between Two Friends and a Lion (Hardcover)",
            "author": "Anthony Bourke",
            "desc": "avg rating 4.06 \u2014 6,835 ratings\u2014 published 1971",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1400728309l/6113349._SY75_.jpg"
        },
        {
            "title": "Arlo: The Lion Who Couldn't Sleep (Hardcover)",
            "author": "Catherine Rayner",
            "desc": "avg rating 3.99 \u2014 377 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1585154852l/50988909._SX50_.jpg"
        },
        {
            "title": "Blackwing Beast (Kane's Mountains, #3)",
            "author": "T.S. Joyce",
            "desc": "avg rating 4.49 \u2014 4,595 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1476379396l/32603703._SY75_.jpg"
        },
        {
            "title": "When an Omega Snaps (A Lion's Pride, #3)",
            "author": "Eve Langlais",
            "desc": "avg rating 4.05 \u2014 3,262 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1431427825l/25525647._SY75_.jpg"
        },
        {
            "title": "As Sure as the Dawn (Mark of the Lion, #3)",
            "author": "Francine Rivers",
            "desc": "avg rating 4.41 \u2014 43,211 ratings\u2014 published 1995",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1490993178l/95621._SX50_.jpg"
        },
        {
            "title": "Ball Of Furry (Ridgeville, #3)",
            "author": "Celia Kyle",
            "desc": "avg rating 3.92 \u2014 2,406 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1444721743l/27162031._SX50_.jpg"
        },
        {
            "title": "You're Lion (Ridgeville, #2)",
            "author": "Celia Kyle",
            "desc": "avg rating 3.88 \u2014 2,122 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1445310446l/27238445._SX50_.jpg"
        },
        {
            "title": "How to Hide a Lion (Hardcover)",
            "author": "Helen Stephens",
            "desc": "avg rating 3.98 \u2014 992 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1356468717l/15943369._SX50_.jpg"
        },
        {
            "title": "Head Over Tail (Ridgeville, #4)",
            "author": "Celia Kyle",
            "desc": "avg rating 4.04 \u2014 2,293 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1444721890l/27162043._SX50_.jpg"
        },
        {
            "title": "The Lion and the Lamb (ebook)",
            "author": "Jenika Snow",
            "desc": "avg rating 3.69 \u2014 1,016 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1375313507l/18216740._SX50_.jpg"
        },
        {
            "title": "Mouse & Lion (Hardcover)",
            "author": "Rand Burkert",
            "desc": "avg rating 4.00 \u2014 444 ratings\u2014 published 2011",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1564855224l/11416722._SX50_.jpg"
        },
        {
            "title": "Valiant (New Species, #3)",
            "author": "Laurann Dohner",
            "desc": "avg rating 4.28 \u2014 24,227 ratings\u2014 published 2011",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1314272985l/12432550._SY75_.jpg"
        },
        {
            "title": "A Voice in the Wind (Mark of the Lion, #1)",
            "author": "Francine Rivers",
            "desc": "avg rating 4.57 \u2014 98,842 ratings\u2014 published 1993",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1459567327l/95617._SX50_.jpg"
        },
        {
            "title": "Savage Fae (Ruthless Boys of the Zodiac, #2)",
            "author": "Caroline Peckham",
            "desc": "avg rating 4.25 \u2014 46,564 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1619382623l/57849105._SY75_.jpg"
        },
        {
            "title": "Dark Fae (Ruthless Boys of the Zodiac, #1)",
            "author": "Caroline Peckham",
            "desc": "avg rating 4.17 \u2014 55,024 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1619705977l/57892054._SY75_.jpg"
        },
        {
            "title": "Sometimes Cake (Hardcover)",
            "author": "Edwina Wyatt",
            "desc": "avg rating 4.08 \u2014 171 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1592291813l/54115088._SX50_.jpg"
        },
        {
            "title": "A Long Way Home (Paperback)",
            "author": "Saroo Brierley",
            "desc": "avg rating 4.12 \u2014 65,703 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1528627384l/18111281._SY75_.jpg"
        },
        {
            "title": "Red Light, Green Lion (Hardcover)",
            "author": "Candace Ryan",
            "desc": "avg rating 3.44 \u2014 192 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1536843211l/41717465._SX50_.jpg"
        },
        {
            "title": "Dandy (Hardcover)",
            "author": "Ame Dyckman",
            "desc": "avg rating 4.45 \u2014 1,379 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1534277504l/39644471._SX50_.jpg"
        },
        {
            "title": "Tarian Silver Lion (New Tarian Pride, #2)",
            "author": "T.S. Joyce",
            "desc": "avg rating 4.44 \u2014 2,386 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1550408634l/44032477._SY75_.jpg"
        },
        {
            "title": "Ash Bear (Daughters of Beasts, #3)",
            "author": "T.S. Joyce",
            "desc": "avg rating 4.54 \u2014 3,086 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1543241265l/42958299._SY75_.jpg"
        },
        {
            "title": "Zebra on the Go (Hardcover)",
            "author": "Jill Nogales",
            "desc": "avg rating 3.50 \u2014 230 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1480689253l/31620951._SX50_.jpg"
        },
        {
            "title": "We're Going on a Lion Hunt (Kindle Edition)",
            "author": "Margery Cuyler",
            "desc": "avg rating 3.99 \u2014 444 ratings\u2014 published 2008",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1393875901l/18799559._SX50_.jpg"
        },
        {
            "title": "Oh, My Roared (Paranormal Dating Agency, #12)",
            "author": "Milly Taiden",
            "desc": "avg rating 4.22 \u2014 2,109 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1483643788l/33800699._SY75_.jpg"
        },
        {
            "title": "Red Havoc Rebel (Red Havoc Panthers, #2)",
            "author": "T.S. Joyce",
            "desc": "avg rating 4.48 \u2014 3,055 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1490104313l/34656137._SY75_.jpg"
        },
        {
            "title": "Walk with Me (Hardcover)",
            "author": "Jairo Buitrago",
            "desc": "avg rating 3.95 \u2014 861 ratings\u2014 published 2008",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1488501279l/25986765._SX50_.jpg"
        },
        {
            "title": "The Lion and the Jewel (Paperback)",
            "author": "Wole Soyinka",
            "desc": "avg rating 3.77 \u2014 1,859 ratings\u2014 published 1959",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1400399539l/2570._SX50_.jpg"
        },
        {
            "title": "In Debt to the King (Shifter Fight League, #1)",
            "author": "Mina Carter",
            "desc": "avg rating 3.80 \u2014 726 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1461435056l/29984220._SY75_.jpg"
        },
        {
            "title": "The Voyage of the Dawn Treader (Chronicles of Narnia, #3)",
            "author": "C.S. Lewis",
            "desc": "avg rating 4.09 \u2014 482,511 ratings\u2014 published 1952",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1661032500l/140225._SX50_.jpg"
        },
        {
            "title": "The Last Battle (Chronicles of Narnia, #7)",
            "author": "C.S. Lewis",
            "desc": "avg rating 4.01 \u2014 286,311 ratings\u2014 published 1956",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1308814830l/84369._SY75_.jpg"
        },
        {
            "title": "The Alion King (Paranormal Dating Agency, #6)",
            "author": "Milly Taiden",
            "desc": "avg rating 4.23 \u2014 4,129 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1437455667l/25812404._SY75_.jpg"
        },
        {
            "title": "Lion Eyes (Shifters Unbound, #7.25)",
            "author": "Jennifer Ashley",
            "desc": "avg rating 4.08 \u2014 2,378 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1436470356l/25774284._SY75_.jpg"
        },
        {
            "title": "The Lion and the Bird (Hardcover)",
            "author": "Marianne Dubuc",
            "desc": "avg rating 4.44 \u2014 2,132 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1400955465l/18528005._SX50_.jpg"
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        }
    ],
    "Vierge": [
        {
            "title": "Fifty Shades of Grey (Fifty Shades, #1)",
            "author": "E.L. James",
            "desc": "avg rating 3.66 \u2014 2,705,721 ratings\u2014 published 2011",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1385207843l/10818853._SX50_.jpg"
        },
        {
            "title": "Playing for Keeps (Neighbor from Hell, #1)",
            "author": "R.L. Mathewson",
            "desc": "avg rating 4.02 \u2014 114,785 ratings\u2014 published 2011",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1406585295l/11381643._SX50_.jpg"
        },
        {
            "title": "The Mistake (Off-Campus, #2)",
            "author": "Elle Kennedy",
            "desc": "avg rating 4.00 \u2014 450,445 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1557835772l/45756920._SY75_.jpg"
        },
        {
            "title": "Archer's Voice (ebook)",
            "author": "Mia Sheridan",
            "desc": "avg rating 4.20 \u2014 551,921 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1656593818l/32822135._SY75_.jpg"
        },
        {
            "title": "Losing It (Losing It, #1)",
            "author": "Cora Carmack",
            "desc": "avg rating 3.72 \u2014 108,769 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348459319l/16034964._SY75_.jpg"
        },
        {
            "title": "Beautiful Disaster (Beautiful, #1)",
            "author": "Jamie McGuire",
            "desc": "avg rating 4.00 \u2014 696,822 ratings\u2014 published 2011",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1358259032l/11505797._SY75_.jpg"
        },
        {
            "title": "Under Locke (Kindle Edition)",
            "author": "Mariana Zapata",
            "desc": "avg rating 3.91 \u2014 94,756 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1390340678l/20613920._SY75_.jpg"
        },
        {
            "title": "Bound by Honor (Born in Blood Mafia Chronicles, #1)",
            "author": "Cora Reilly",
            "desc": "avg rating 3.78 \u2014 112,503 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1582304059l/51525075._SX50_.jpg"
        },
        {
            "title": "Fallen Too Far (Rosemary Beach, #1; Too Far, #1)",
            "author": "Abbi Glines",
            "desc": "avg rating 4.15 \u2014 173,201 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1349565157l/16070903._SY75_.jpg"
        },
        {
            "title": "Wrong (Cafe, #1)",
            "author": "Jana Aston",
            "desc": "avg rating 3.82 \u2014 49,188 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1487134024l/26850194._SY75_.jpg"
        },
        {
            "title": "Bully (Fall Away, #1)",
            "author": "Penelope Douglas",
            "desc": "avg rating 3.86 \u2014 210,916 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1678294316l/123206634._SX50_.jpg"
        },
        {
            "title": "The Kiss Thief (Paperback)",
            "author": "L.J. Shen",
            "desc": "avg rating 3.85 \u2014 110,851 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1544101164l/41450662._SY75_.jpg"
        },
        {
            "title": "Breathe (Colorado Mountain, #4)",
            "author": "Kristen Ashley",
            "desc": "avg rating 4.33 \u2014 38,250 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1389219809l/20494223._SY75_.jpg"
        },
        {
            "title": "Rule (Marked Men, #1)",
            "author": "Jay Crownover",
            "desc": "avg rating 4.11 \u2014 101,190 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1357012113l/17200687._SX50_.jpg"
        },
        {
            "title": "Kiss an Angel (Paperback)",
            "author": "Susan Elizabeth Phillips",
            "desc": "avg rating 4.17 \u2014 66,740 ratings\u2014 published 1996",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1309115033l/73086._SY75_.jpg"
        },
        {
            "title": "Nero (Alliance, #1)",
            "author": "S.J. Tilly",
            "desc": "avg rating 3.87 \u2014 59,864 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1674780586l/85164835._SY75_.jpg"
        },
        {
            "title": "Lassoing the Virgin Mail-Order Bride (Cowboys & Virgins, #1)",
            "author": "Alexa Riley",
            "desc": "avg rating 3.86 \u2014 8,477 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1458226900l/29541068._SY75_.jpg"
        },
        {
            "title": "Until Nico (Until, #4)",
            "author": "Aurora Rose Reynolds",
            "desc": "avg rating 4.28 \u2014 30,909 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1398781346l/18781543._SY75_.jpg"
        },
        {
            "title": "Sweet Temptation (Kindle Edition)",
            "author": "Cora Reilly",
            "desc": "avg rating 4.00 \u2014 74,517 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1583736804l/52226559._SY75_.jpg"
        },
        {
            "title": "Coach (Breeding, #1)",
            "author": "Alexa Riley",
            "desc": "avg rating 3.48 \u2014 14,196 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1442200212l/26310515._SY75_.jpg"
        },
        {
            "title": "Blind Side (Red Zone Rivals, #2)",
            "author": "Kandi Steiner",
            "desc": "avg rating 3.98 \u2014 74,406 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1654024903l/60633773._SY75_.jpg"
        },
        {
            "title": "Wait for You (Wait for You, #1)",
            "author": "J. Lynn",
            "desc": "avg rating 4.13 \u2014 166,525 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1363819713l/17314430._SY75_.jpg"
        },
        {
            "title": "The Pucking Wrong Number (Pucking Wrong, #1)",
            "author": "C.R. Jane",
            "desc": "avg rating 3.55 \u2014 59,671 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1688010577l/123414004._SX50_.jpg"
        },
        {
            "title": "Credence (Paperback)",
            "author": "Penelope Douglas",
            "desc": "avg rating 3.68 \u2014 422,279 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1576590268l/49084724._SX50_.jpg"
        },
        {
            "title": "The Game Plan (Game On, #3)",
            "author": "Kristen Callihan",
            "desc": "avg rating 4.06 \u2014 32,944 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1445605918l/23204215._SY75_.jpg"
        },
        {
            "title": "In Flight (Up in the Air, #1)",
            "author": "R.K. Lilley",
            "desc": "avg rating 4.07 \u2014 78,785 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1533596732l/41060893._SY75_.jpg"
        },
        {
            "title": "A Hunger Like No Other (Immortals After Dark, #1)",
            "author": "Kresley Cole",
            "desc": "avg rating 4.09 \u2014 87,403 ratings\u2014 published 2006",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1357616154l/14384._SY75_.jpg"
        },
        {
            "title": "Gabriel's Inferno (Gabriel's Inferno, #1)",
            "author": "Sylvain Reynard",
            "desc": "avg rating 3.98 \u2014 159,577 ratings\u2014 published 2011",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1301789770l/10140661._SY75_.jpg"
        },
        {
            "title": "Blindsided (Harris Brothers World, #2)",
            "author": "Amy Daws",
            "desc": "avg rating 4.07 \u2014 46,564 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1573013361l/52602989._SX50_SY75_.jpg"
        },
        {
            "title": "Crow (Boston Underworld, #1)",
            "author": "A. Zavarelli",
            "desc": "avg rating 4.03 \u2014 29,741 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1704283959l/204781435._SY75_.jpg"
        },
        {
            "title": "Hopeless (Chestnut Springs, #5)",
            "author": "Elsie Silver",
            "desc": "avg rating 4.12 \u2014 201,333 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1691767240l/174753697._SY75_.jpg"
        },
        {
            "title": "Welcome to the Dark Side (The Fallen Men, #2)",
            "author": "Giana Darling",
            "desc": "avg rating 4.11 \u2014 32,069 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1582152627l/51480780._SY75_.jpg"
        },
        {
            "title": "The V Girl: A Coming of Age Story (Kindle Edition)",
            "author": "Mya Robarts",
            "desc": "avg rating 3.98 \u2014 16,278 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1688009281l/25437891._SY75_.jpg"
        },
        {
            "title": "Transcendence (Transcendence, #1)",
            "author": "Shay Savage",
            "desc": "avg rating 4.03 \u2014 23,668 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1391320052l/20504754._SY75_.jpg"
        },
        {
            "title": "Twist Me (Twist Me, #1)",
            "author": "Anna Zaires",
            "desc": "avg rating 3.87 \u2014 30,749 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1473195225l/31847592._SY75_.jpg"
        },
        {
            "title": "Shielding Lily (Kindle Edition)",
            "author": "Alexa Riley",
            "desc": "avg rating 3.96 \u2014 9,683 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1473183450l/31752057._SY75_.jpg"
        },
        {
            "title": "Sparrow (Boston Belles, #0.5)",
            "author": "L.J. Shen",
            "desc": "avg rating 4.04 \u2014 55,118 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1454909563l/27263454._SY75_.jpg"
        },
        {
            "title": "Sacked (Gridiron, #1)",
            "author": "Jen Frederick",
            "desc": "avg rating 3.98 \u2014 17,267 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1438723430l/25904855._SX50_.jpg"
        },
        {
            "title": "Protecting What's His (Line of Duty, #1)",
            "author": "Tessa Bailey",
            "desc": "avg rating 3.77 \u2014 24,923 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1396557274l/17413427._SX50_.jpg"
        },
        {
            "title": "Devil in Winter (Wallflowers, #3)",
            "author": "Lisa Kleypas",
            "desc": "avg rating 4.21 \u2014 92,409 ratings\u2014 published 2006",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1309220205l/114166._SY75_.jpg"
        },
        {
            "title": "Mechanic (Breeding, #2)",
            "author": "Alexa Riley",
            "desc": "avg rating 3.64 \u2014 13,864 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1446894314l/27556157._SY75_.jpg"
        },
        {
            "title": "Filthy Beautiful Lies (Filthy Beautiful Lies, #1)",
            "author": "Kendall Ryan",
            "desc": "avg rating 3.98 \u2014 23,096 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1576527893l/49333890._SY75_.jpg"
        },
        {
            "title": "Stepbrother Dearest (Paperback)",
            "author": "Penelope Ward",
            "desc": "avg rating 4.03 \u2014 71,731 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1407407844l/22843341._SY75_.jpg"
        },
        {
            "title": "Nero (Made Men, #1)",
            "author": "Sarah Brianne",
            "desc": "avg rating 4.00 \u2014 24,037 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1402969198l/22494969._SY75_.jpg"
        },
        {
            "title": "Escorted (Escorted, #1)",
            "author": "Claire Kent",
            "desc": "avg rating 3.91 \u2014 13,474 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1607142812l/56165680._SY75_.jpg"
        },
        {
            "title": "His Princess (The Princess, #1)",
            "author": "Alexa Riley",
            "desc": "avg rating 3.65 \u2014 9,847 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1487711994l/34370044._SY75_.jpg"
        },
        {
            "title": "Tempt Me (The Wolf Hotel, #1)",
            "author": "NinaWest",
            "desc": "avg rating 3.92 \u2014 54,252 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1606575776l/56071741._SY75_.jpg"
        },
        {
            "title": "Bound by Duty (Born in Blood Mafia Chronicles, #2)",
            "author": "Cora Reilly",
            "desc": "avg rating 3.79 \u2014 66,039 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1582555936l/51661616._SX50_.jpg"
        },
        {
            "title": "Devil's Game (Reapers MC, #3)",
            "author": "Joanna Wylde",
            "desc": "avg rating 4.26 \u2014 29,206 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1433115819l/18693621._SY75_.jpg"
        },
        {
            "title": "At Any Price (Gaming the System, #1)",
            "author": "Brenna Aubrey",
            "desc": "avg rating 3.90 \u2014 20,713 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1507528953l/36379678._SY75_.jpg"
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        }
    ],
    "Balance": [
        {
            "title": "Never Let Me Go (Paperback)",
            "author": "Kazuo Ishiguro",
            "desc": "avg rating 3.85 \u2014 747,066 ratings\u2014 published 2005",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1353048590l/6334._SY75_.jpg"
        },
        {
            "title": "All About Love: New Visions (Hardcover)",
            "author": "bell hooks",
            "desc": "avg rating 4.04 \u2014 102,945 ratings\u2014 published 1999",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1387754966l/17607._SY75_.jpg"
        },
        {
            "title": "Natural Beauty (Hardcover)",
            "author": "Ling Ling Huang",
            "desc": "avg rating 3.80 \u2014 15,110 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1659407685l/61420120._SX50_.jpg"
        },
        {
            "title": "Thirst for Salt (Paperback)",
            "author": "Madelaine Lucas",
            "desc": "avg rating 3.84 \u2014 5,581 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1671854311l/61340225._SY75_.jpg"
        },
        {
            "title": "Timecode of a Face (Paperback)",
            "author": "Ruth Ozeki",
            "desc": "avg rating 4.00 \u2014 2,786 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1651339595l/60908555._SY75_.jpg"
        },
        {
            "title": "The Waves (Paperback)",
            "author": "Virginia Woolf",
            "desc": "avg rating 4.15 \u2014 47,037 ratings\u2014 published 1931",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1645526068l/46114._SY75_.jpg"
        },
        {
            "title": "Invisible Cities (Paperback)",
            "author": "Italo Calvino",
            "desc": "avg rating 4.11 \u2014 88,146 ratings\u2014 published 1972",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1468623303l/9809._SY75_.jpg"
        },
        {
            "title": "Honey & Spice (Hardcover)",
            "author": "Bolu Babalola",
            "desc": "avg rating 3.92 \u2014 38,302 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1657036504l/59088365._SY75_.jpg"
        },
        {
            "title": "The Martyrology Books 1 & 2 (Paperback)",
            "author": "bpNichol",
            "desc": "avg rating 4.08 \u2014 77 ratings\u2014 published 1972",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1280803111l/403197._SY75_.jpg"
        },
        {
            "title": "The Book of Laughter and Forgetting (Paperback)",
            "author": "Milan Kundera",
            "desc": "avg rating 3.96 \u2014 51,193 ratings\u2014 published 1979",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1614905132l/240976._SY75_.jpg"
        },
        {
            "title": "The Love Hypothesis (Paperback)",
            "author": "Ali Hazelwood",
            "desc": "avg rating 4.13 \u2014 1,531,326 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1611937942l/56732449._SX50_.jpg"
        },
        {
            "title": "Beach Read (Paperback)",
            "author": "Emily Henry",
            "desc": "avg rating 4.00 \u2014 1,327,154 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1589881197l/52867387._SX50_.jpg"
        },
        {
            "title": "Girl, Woman, Other (Kindle Edition)",
            "author": "Bernardine Evaristo",
            "desc": "avg rating 4.28 \u2014 244,338 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1542296262l/41081373._SY75_.jpg"
        },
        {
            "title": "A History of My Brief Body (Kindle Edition)",
            "author": "Billy-Ray Belcourt",
            "desc": "avg rating 4.20 \u2014 5,067 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1599268029l/44049371._SX50_.jpg"
        },
        {
            "title": "We Were Liars (Kindle Edition)",
            "author": "E. Lockhart",
            "desc": "avg rating 3.66 \u2014 1,206,642 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1402749479l/16143347._SY75_.jpg"
        },
        {
            "title": "Kafka on the Shore (Paperback)",
            "author": "Haruki Murakami",
            "desc": "avg rating 4.13 \u2014 497,068 ratings\u2014 published 2002",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1429638085l/4929._SY75_.jpg"
        },
        {
            "title": "A Discovery: Love and Other Things (ebook)",
            "author": "VictoriaWoods",
            "desc": "avg rating 3.79 \u2014 240 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1691728208l/123184581._SY75_.jpg"
        },
        {
            "title": "The Great Believers (Paperback)",
            "author": "Rebecca Makkai",
            "desc": "avg rating 4.29 \u2014 148,247 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1556229367l/45304101._SY75_.jpg"
        },
        {
            "title": "The Fifth Season (The Broken Earth, #1)",
            "author": "N.K. Jemisin",
            "desc": "avg rating 4.30 \u2014 290,617 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1386803701l/19161852._SY75_.jpg"
        },
        {
            "title": "Bound by Their Lisbon Legacy (Harlequin Romance, 4910)",
            "author": "Ella Hayes",
            "desc": "avg rating 4.10 \u2014 10 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1717005736l/200699911._SX50_.jpg"
        },
        {
            "title": "The Girl with the Dragon Tattoo (Millennium, #1)",
            "author": "Stieg Larsson",
            "desc": "avg rating 4.17 \u2014 3,272,188 ratings\u2014 published 2005",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1684638853l/2429135._SX50_.jpg"
        },
        {
            "title": "That Librarian: The Fight Against Book Banning in America (Hardcover)",
            "author": "AmandaJones",
            "desc": "avg rating 3.97 \u2014 1,401 ratings\u2014 published 2024",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1710358438l/203579067._SY75_.jpg"
        },
        {
            "title": "The God of the Woods (Kindle Edition)",
            "author": "LizMoore",
            "desc": "avg rating 4.19 \u2014 172,585 ratings\u2014 published 2024",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1717970538l/199698485._SY75_.jpg"
        },
        {
            "title": "Flying Point: One Writer's Journey Into Solitude (Kindle Edition)",
            "author": "Susan D.Anderson",
            "desc": "avg rating 4.20 \u2014 10 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1506349400l/36302305._SY75_.jpg"
        },
        {
            "title": "The Apollo Murders (Apollo Murders, #1)",
            "author": "Chris Hadfield",
            "desc": "avg rating 3.92 \u2014 16,818 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1629112133l/57007683._SY75_.jpg"
        },
        {
            "title": "Klara and the Sun (Hardcover)",
            "author": "Kazuo Ishiguro",
            "desc": "avg rating 3.74 \u2014 371,373 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1603206535l/54120408._SY75_.jpg"
        },
        {
            "title": "The Nix (Hardcover)",
            "author": "NathanHill",
            "desc": "avg rating 4.08 \u2014 79,474 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1474083394l/28251002._SY75_.jpg"
        },
        {
            "title": "Fruto",
            "author": "Daniela Rea",
            "desc": "avg rating 4.61 \u2014 1,110 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1675963407l/108293577._SY75_.jpg"
        },
        {
            "title": "Lo que hay (Paperback)",
            "author": "SaraTorres",
            "desc": "avg rating 3.99 \u2014 5,418 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1650193242l/60827741._SY75_.jpg"
        },
        {
            "title": "Los nombres propios (Paperback)",
            "author": "Marta Jim\u00e9nez Serrano",
            "desc": "avg rating 4.32 \u2014 6,940 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1718085132l/57398262._SY75_.jpg"
        },
        {
            "title": "Canto yo y la monta\u00f1a baila (Paperback)",
            "author": "Irene Sol\u00e0",
            "desc": "avg rating 4.24 \u2014 24,855 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1559139214l/45479298._SY75_.jpg"
        },
        {
            "title": "Por qu\u00e9 volv\u00edas cada verano (Paperback)",
            "author": "Bel\u00e9n L\u00f3pez Peir\u00f3",
            "desc": "avg rating 4.23 \u2014 4,440 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1650196929l/40510899._SY75_.jpg"
        },
        {
            "title": "Fierce Attachments (Paperback)",
            "author": "Vivian Gornick",
            "desc": "avg rating 4.05 \u2014 16,379 ratings\u2014 published 1987",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1316635674l/177333._SX50_.jpg"
        },
        {
            "title": "Spring 58: A Journal of Archetype and Culture (Paperback)",
            "author": "James Hillman",
            "desc": "(editor)",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1182010191l/1222453.jpg"
        },
        {
            "title": "The Roses & The Windows (Hardcover)",
            "author": "Rainer Maria Rilke",
            "desc": "avg rating 4.07 \u2014 27 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1438708501l/26039903._SX50_.jpg"
        },
        {
            "title": "Your Perfect Right: Assertiveness and Equality in Your Life and Relationships (Paperback)",
            "author": "Robert Alberti",
            "desc": "avg rating 3.71 \u2014 589 ratings\u2014 published 1970",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1485242148l/33977133._SY75_.jpg"
        },
        {
            "title": "\u03a3\u03c5\u03bd\u03bd\u03b5\u03c6\u03b9\u03ac\u03b6\u03b5\u03b9 (Paperback)",
            "author": "Menelaos Lountemis",
            "desc": "avg rating 3.25 \u2014 4 ratings\u2014 published",
            "img": "https://s.gr-assets.com/assets/nophoto/book/50x75-a91bf249278a81aabab721ef782c4a74.png"
        },
        {
            "title": "Days at the Morisaki Bookshop (Days at the Morisaki Bookshop, #1)",
            "author": "Satoshi Yagisawa",
            "desc": "avg rating 3.65 \u2014 104,384 ratings\u2014 published 2010",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1671208761l/62047992._SY75_.jpg"
        },
        {
            "title": "The da Vinci Code (Robert Langdon, #2)",
            "author": "Dan Brown",
            "desc": "avg rating 3.92 \u2014 2,409,255 ratings\u2014 published 2003",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1720313229l/968._SY75_.jpg"
        },
        {
            "title": "Descolonizando afetos: Experimenta\u00e7\u00f5es sobre outras formas de amar (Kindle Edition)",
            "author": "Geni Nu\u00f1ez",
            "desc": "avg rating 4.39 \u2014 377 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1697048410l/199406095._SY75_.jpg"
        },
        {
            "title": "Pensamiento mon\u00f3gamo, terror poliamoroso (Paperback)",
            "author": "Brigitte Vasallo",
            "desc": "avg rating 4.27 \u2014 2,424 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1550139404l/43068774._SY75_.jpg"
        },
        {
            "title": "La invenci\u00f3n de las mujeres: Una perspectiva africana sobre los discursos occidentales de g\u00e9nero (Paperback)",
            "author": "Oy\u00e8r\u00f3nk\u1eb9\u0301 Oy\u011bw\u00f9m\u00ed",
            "desc": "avg rating 4.80 \u2014 5 ratinngs\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1699171178l/123699240._SY75_.jpg"
        },
        {
            "title": "Polysecure: Attachment, Trauma and Consensual Nonmonogamy (Paperback)",
            "author": "Jessica Fern",
            "desc": "avg rating 4.39 \u2014 12,606 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1598102750l/52569124._SY75_.jpg"
        },
        {
            "title": "Aire de las colinas: Cartas a Clara (Hardcover)",
            "author": "Juan Rulfo",
            "desc": "avg rating 4.31 \u2014 567 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1256937298l/38789._SX50_.jpg"
        },
        {
            "title": "The Straight Mind: And Other Essays (Paperback)",
            "author": "Monique Wittig",
            "desc": "avg rating 4.16 \u2014 2,131 ratings\u2014 published 1980",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1320492186l/416129._SY75_.jpg"
        },
        {
            "title": "Barbarian Days: A Surfing Life (Hardcover)",
            "author": "William Finnegan",
            "desc": "avg rating 4.27 \u2014 34,640 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1418768620l/18693910._SX50_.jpg"
        },
        {
            "title": "Yellowface (Hardcover)",
            "author": "R.F. Kuang",
            "desc": "avg rating 3.76 \u2014 673,183 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1671336608l/62047984._SY75_.jpg"
        },
        {
            "title": "The Persians (Paperback)",
            "author": "Aeschylus",
            "desc": "avg rating 3.60 \u2014 4,358 ratings\u2014 published -472",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348628920l/237794._SX50_.jpg"
        },
        {
            "title": "I Have Some Questions for You (Hardcover)",
            "author": "Rebecca Makkai",
            "desc": "avg rating 3.60 \u2014 121,950 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1658970269l/61053829._SY75_.jpg"
        },
        {
            "title": "The Absolute at Large (Paperback)",
            "author": "Karel \u010capek",
            "desc": "avg rating 3.85 \u2014 3,165 ratings\u2014 published 1922",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1328819033l/816445._SY75_.jpg"
        }
    ],
    "Scorpion": [
        {
            "title": "The House of the Scorpion (Matteo Alacran, #1)",
            "author": "Nancy Farmer",
            "desc": "avg rating 4.08 \u2014 93,773 ratings\u2014 published 2002",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1401734230l/13376._SY75_.jpg"
        },
        {
            "title": "Le Masque de la V\u00e9rit\u00e9 (Le Scorpion, #9)",
            "author": "Stephen Desberg",
            "desc": "avg rating 4.01 \u2014 170 ratings\u2014 published 2010",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1322179534l/8690225._SX50_.jpg"
        },
        {
            "title": "L'Ombre de l'Ange (Le Scorpion, #8)",
            "author": "Stephen Desberg",
            "desc": "avg rating 3.91 \u2014 190 ratings\u2014 published 2008",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1241132301l/5664557._SX50_.jpg"
        },
        {
            "title": "Au Nom du P\u00e8re (Le Scorpion, #7)",
            "author": "Stephen Desberg",
            "desc": "avg rating 3.97 \u2014 199 ratings\u2014 published 2006",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327774013l/6605258._SX50_.jpg"
        },
        {
            "title": "La Vall\u00e9e Sacr\u00e9e (Le Scorpion, #5)",
            "author": "Stephen Desberg",
            "desc": "avg rating 3.91 \u2014 253 ratings\u2014 published 2004",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327775561l/2777517._SX50_.jpg"
        },
        {
            "title": "A Text Book of Agada Tantra (Paperback)",
            "author": "U.R. Sekhar Namburi",
            "desc": "avg rating 4.14 \u2014 7 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1526899355l/40186434._SX50_.jpg"
        },
        {
            "title": "Scorpion Deception (Scorpion, #4)",
            "author": "Andrew Kaplan",
            "desc": "avg rating 4.08 \u2014 154 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1362371130l/16065608._SY75_.jpg"
        },
        {
            "title": "Scorpion Betrayal (Scorpion, #2)",
            "author": "Andrew Kaplan",
            "desc": "avg rating 3.72 \u2014 390 ratings\u2014 published 1985",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348217448l/12672472._SY75_.jpg"
        },
        {
            "title": "Gifting Me To His Best Friend (A Touch of Taboo, #2)",
            "author": "Katee Robert",
            "desc": "avg rating 3.74 \u2014 20,998 ratings\u2014 published 2020",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1589391537l/53408227._SY75_.jpg"
        },
        {
            "title": "The Scorpion, Volume 1: The Devil's Mark (Paperback)",
            "author": "Stephen Desberg",
            "desc": "avg rating 3.77 \u2014 82 ratings\u2014 published 2008",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1347378976l/5488890._SX50_.jpg"
        },
        {
            "title": "Le D\u00e9mon au Vatican (Le Scorpion, #4)",
            "author": "Stephen Desberg",
            "desc": "avg rating 3.88 \u2014 243 ratings\u2014 published 2004",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1188594222l/1805731._SX50_.jpg"
        },
        {
            "title": "The Anatomy of a Scorpion: Illustrating the Wheel of Nature (Paperback)",
            "author": "Ira L. Milligan",
            "desc": "avg rating 4.75 \u2014 4 ratings\u2014 published 2000",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1543329675l/2127013._SY75_.jpg"
        },
        {
            "title": "Tangled in Tinsel (The More the Merrier, #1)",
            "author": "Trilina Pucci",
            "desc": "avg rating 3.91 \u2014 38,792 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1662121594l/62221702._SY75_.jpg"
        },
        {
            "title": "Electric Idol (Dark Olympus, #2)",
            "author": "Katee Robert",
            "desc": "avg rating 3.96 \u2014 107,656 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1629300986l/57661359._SX50_.jpg"
        },
        {
            "title": "Tis the Season for Revenge (Seasons of Revenge, #1)",
            "author": "MorganElizabeth",
            "desc": "avg rating 3.93 \u2014 87,076 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1665238477l/61195387._SY75_.jpg"
        },
        {
            "title": "A Very Krampus Holiday (Kindle Edition)",
            "author": "Katee Robert",
            "desc": "avg rating 3.34 \u2014 4,227 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1664031689l/62703657._SY75_.jpg"
        },
        {
            "title": "Neon Gods (Dark Olympus, #1)",
            "author": "Katee Robert",
            "desc": "avg rating 3.70 \u2014 270,213 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1610505010l/54659771._SX50_.jpg"
        },
        {
            "title": "The Scorpion's Mate (Iriduan Test Subjects, #1)",
            "author": "Susan Trombley",
            "desc": "avg rating 3.76 \u2014 4,856 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1518829753l/38601826._SY75_.jpg"
        },
        {
            "title": "Le Tr\u00e9sor du Temple (Le Scorpion, #6)",
            "author": "Stephen Desberg",
            "desc": "avg rating 3.91 \u2014 230 ratings\u2014 published 2002",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327774386l/2777571._SX50_.jpg"
        },
        {
            "title": "The Devil in the Vatican (The Scorpion Vol. 2)",
            "author": "Stephen Desberg",
            "desc": "avg rating 4.02 \u2014 66 ratings\u2014 published 2001",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1347441572l/7273877._SX50_.jpg"
        },
        {
            "title": "La Marque du Diable (Le Scorpion, #1)",
            "author": "Stephen Desberg",
            "desc": "avg rating 3.88 \u2014 434 ratings\u2014 published 2000",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1241094939l/2491085._SX50_.jpg"
        },
        {
            "title": "Amazing Spider-Man (1963-1998) #20",
            "author": "Stan Lee",
            "desc": "avg rating 3.87 \u2014 165 ratings\u2014 published 1965",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1435756669l/25830567._SY75_.jpg"
        },
        {
            "title": "An Outline of a New Star Wisdom (Paperback)",
            "author": "Willi Sucher",
            "desc": "avg rating 4.75 \u2014 4 ratings\u2014 published 1996",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1677797893l/5683798._SX50_.jpg"
        },
        {
            "title": "Blind Scorpion, Iran's Nuclear Sting - Book 2: He could walk away a hero...but for which country? (Kindle Edition)",
            "author": "Mike Wells",
            "desc": "avg rating 4.27 \u2014 11 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1437763266l/25972187._SY75_.jpg"
        },
        {
            "title": "Harry Potter and the Cursed Child: Parts One and Two (Harry Potter, #8)",
            "author": "J.K. Rowling",
            "desc": "avg rating 3.48 \u2014 1,062,718 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1470082995l/29056083._SY75_.jpg"
        },
        {
            "title": "Predators! (Know-It-Alls)",
            "author": "Kenn Goin",
            "desc": "avg rating 4.22 \u2014 9 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1267896096l/7694825._SX50_.jpg"
        },
        {
            "title": "The Light Between Oceans (Hardcover)",
            "author": "M.L. Stedman",
            "desc": "avg rating 4.04 \u2014 465,533 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1336683021l/13158800._SY75_.jpg"
        },
        {
            "title": "The Adoration of Jenna Fox (Jenna Fox Chronicles, #1)",
            "author": "Mary E. Pearson",
            "desc": "avg rating 3.69 \u2014 52,369 ratings\u2014 published 2008",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388715600l/1902241._SY75_.jpg"
        },
        {
            "title": "Jody Richards and the Secret Potion (Kindle Edition)",
            "author": "Tony Flood",
            "desc": "avg rating 4.59 \u2014 17 ratings\u2014 published 2009",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1328338699l/11422049._SX50_.jpg"
        },
        {
            "title": "The Icky Bug Alphabet Book (Hardcover)",
            "author": "Jerry Pallotta",
            "desc": "avg rating 3.93 \u2014 321 ratings\u2014 published 1986",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1389593417l/991982._SX50_.jpg"
        },
        {
            "title": "Robin Hood: Outlaw of Sherwood Forest [An English Legend] (Graphic Myths and Legends)",
            "author": "Paul D. Storrie",
            "desc": "avg rating 3.91 \u2014 118 ratings\u2014 published 2004",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1391288463l/20689732._SX50_.jpg"
        },
        {
            "title": "Lunch Lady and the Cyborg Substitute (Lunch Lady, #1)",
            "author": "Jarrett J. Krosoczka",
            "desc": "avg rating 4.03 \u2014 13,471 ratings\u2014 published 2009",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1320460406l/6277757._SX50_.jpg"
        },
        {
            "title": "Diary of a Wimpy Kid (Diary of a Wimpy Kid, #1)",
            "author": "Jeff Kinney",
            "desc": "avg rating 3.98 \u2014 716,255 ratings\u2014 published 2007",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388183826l/389627._SX50_.jpg"
        },
        {
            "title": "Whales on Stilts (Pals in Peril, #1)",
            "author": "M.T. Anderson",
            "desc": "avg rating 3.66 \u2014 2,072 ratings\u2014 published 2005",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1320408050l/538838._SX50_.jpg"
        },
        {
            "title": "Charlie and the Chocolate Factory (Charlie Bucket, #1)",
            "author": "Roald Dahl",
            "desc": "avg rating 4.16 \u2014 875,768 ratings\u2014 published 1964",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1309211401l/6310._SY75_.jpg"
        },
        {
            "title": "The Story of Abraham Lincoln: President for the People (Famous Lives)",
            "author": "Larry Weinberg",
            "desc": "avg rating 3.27 \u2014 11 ratings\u2014 published 1991",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1266949029l/1982989._SY75_.jpg"
        },
        {
            "title": "Skeleton Man (Skeleton Man, #1)",
            "author": "Joseph Bruchac",
            "desc": "avg rating 3.82 \u2014 3,319 ratings\u2014 published 2001",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348938430l/670080._SY75_.jpg"
        },
        {
            "title": "Rodrick Rules (Diary of a Wimpy Kid, #2)",
            "author": "Jeff Kinney",
            "desc": "avg rating 4.16 \u2014 184,415 ratings\u2014 published 2008",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1360095964l/1809465._SX50_.jpg"
        },
        {
            "title": "The Tale of Despereaux (Paperback)",
            "author": "Kate DiCamillo",
            "desc": "avg rating 4.07 \u2014 204,493 ratings\u2014 published 2003",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1412211823l/37190._SX50_.jpg"
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        }
    ],
    "Sagittaire": [
        {
            "title": "The Colony (Hardcover)",
            "author": "Audrey Magee",
            "desc": "avg rating 4.11 \u2014 10,696 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1634231936l/57977494._SY75_.jpg"
        },
        {
            "title": "Small Things Like These (Hardcover)",
            "author": "Claire Keegan",
            "desc": "avg rating 4.18 \u2014 212,514 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1627655660l/58662236._SX50_.jpg"
        },
        {
            "title": "Greenwood (Hardcover)",
            "author": "Michael Christie",
            "desc": "avg rating 4.33 \u2014 24,629 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1567105359l/39328584._SY75_.jpg"
        },
        {
            "title": "Sula (Paperback)",
            "author": "Toni Morrison",
            "desc": "avg rating 4.04 \u2014 107,277 ratings\u2014 published 1973",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1441578153l/11346._SY75_.jpg"
        },
        {
            "title": "Alice\u2019s Adventures in Wonderland / Through the Looking-Glass (Paperback)",
            "author": "Lewis Carroll",
            "desc": "avg rating 4.06 \u2014 579,753 ratings\u2014 published 1871",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1630487234l/24213._SX50_.jpg"
        },
        {
            "title": "All the Light We Cannot See (Hardcover)",
            "author": "Anthony Doerr",
            "desc": "avg rating 4.31 \u2014 1,777,404 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1451445646l/18143977._SY75_.jpg"
        },
        {
            "title": "Americanah (Hardcover)",
            "author": "Chimamanda Ngozi Adichie",
            "desc": "avg rating 4.32 \u2014 385,276 ratings\u2014 published 2013",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1356654499l/15796700._SX50_.jpg"
        },
        {
            "title": "Astro Poets: Your Guides to the Zodiac (Hardcover)",
            "author": "Alex Dimitrov",
            "desc": "avg rating 3.74 \u2014 1,098 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1556895576l/43263660._SY75_.jpg"
        },
        {
            "title": "The Anthropologists (Hardcover)",
            "author": "Ayseg\u00fcl Savas",
            "desc": "avg rating 3.96 \u2014 1,463 ratings\u2014 published 2024",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1702650641l/195391751._SY75_.jpg"
        },
        {
            "title": "Rest Is Resistance: A Manifesto (Hardcover)",
            "author": "Tricia Hersey",
            "desc": "avg rating 4.08 \u2014 9,695 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1664244996l/60382737._SY75_.jpg"
        },
        {
            "title": "Circe (Hardcover)",
            "author": "Madeline Miller",
            "desc": "avg rating 4.23 \u2014 1,158,720 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1565909496l/35959740._SY75_.jpg"
        },
        {
            "title": "The Monk Who Sold His Ferrari: A Fable About Fulfilling Your Dreams and Reaching Your Destiny (Paperback)",
            "author": "Robin S. Sharma",
            "desc": "avg rating 3.89 \u2014 167,864 ratings\u2014 published 1996",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388189325l/43877._SY75_.jpg"
        },
        {
            "title": "Samsara, Nirvana, and Buddha Nature (3) (The Library of Wisdom and Compassion)",
            "author": "Dalai Lama XIV",
            "desc": "avg rating 4.55 \u2014 47 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1545520215l/40637724._SY75_.jpg"
        },
        {
            "title": "Fourth Wing (The Empyrean, #1)",
            "author": "Rebecca Yarros",
            "desc": "avg rating 4.57 \u2014 2,169,931 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1701980900l/61431922._SY75_.jpg"
        },
        {
            "title": "Women Who Run With the Wolves (Paperback)",
            "author": "Clarissa Pinkola Est\u00e9s",
            "desc": "avg rating 4.12 \u2014 82,176 ratings\u2014 published 1992",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1662139742l/241823._SY75_.jpg"
        },
        {
            "title": "Giordano Bruno and the Hermetic Tradition (Hardcover)",
            "author": "Frances A. Yates",
            "desc": "avg rating 4.35 \u2014 648 ratings\u2014 published 1964",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1172913322l/230361._SY75_.jpg"
        },
        {
            "title": "The Art of Memory (Paperback)",
            "author": "Frances A. Yates",
            "desc": "avg rating 4.16 \u2014 1,534 ratings\u2014 published 1966",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388724015l/245831._SY75_.jpg"
        },
        {
            "title": "Blood Syndicate (1993-1995) #4",
            "author": "Iv\u00e1n V\u00e9lez, Jr.",
            "desc": "avg rating 3.50 \u2014 4 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1619069247l/57816804._SY75_.jpg"
        },
        {
            "title": "Blood Syndicate (1993-1995) #3",
            "author": "Dwayne McDuffie",
            "desc": "avg rating 3.67 \u2014 3 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1617862496l/57664516._SY75_.jpg"
        },
        {
            "title": "Blood Syndicate (1993-1995) #2",
            "author": "Dwayne McDuffie",
            "desc": "avg rating 4.00 \u2014 4 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1616651132l/57521327._SY75_.jpg"
        },
        {
            "title": "Blood Syndicate (1993-1995) #1",
            "author": "Dwayne McDuffie",
            "desc": "avg rating 4.10 \u2014 10 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1615453473l/57374991._SY75_.jpg"
        },
        {
            "title": "Static Shock: Trial by Fire (Paperback)",
            "author": "Dwayne McDuffie",
            "desc": "avg rating 3.88 \u2014 108 ratings\u2014 published 2000",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1307746844l/1009286._SX50_.jpg"
        },
        {
            "title": "The Selection (The Selection, #1)",
            "author": "Kiera Cass",
            "desc": "avg rating 4.08 \u2014 1,629,781 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1322103400l/10507293._SY75_.jpg"
        },
        {
            "title": "Tao Te Ching (Paperback)",
            "author": "Lao Tzu",
            "desc": "avg rating 4.30 \u2014 164,275 ratings\u2014 published -350",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1333578861l/67896._SY75_.jpg"
        },
        {
            "title": "The Nicomachean Ethics (Paperback)",
            "author": "Aristotle",
            "desc": "avg rating 3.99 \u2014 52,734 ratings\u2014 published -350",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1520339295l/19068._SY75_.jpg"
        },
        {
            "title": "A History of Western Philosophy (Paperback)",
            "author": "Bertrand Russell",
            "desc": "avg rating 4.13 \u2014 39,971 ratings\u2014 published 1945",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1709106488l/243685._SY75_.jpg"
        },
        {
            "title": "Meditations (Paperback)",
            "author": "Marcus Aurelius",
            "desc": "avg rating 4.28 \u2014 278,036 ratings\u2014 published 180",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1421618636l/30659._SY75_.jpg"
        },
        {
            "title": "The Scarlet Letter (Paperback)",
            "author": "Nathaniel Hawthorne",
            "desc": "avg rating 3.43 \u2014 882,604 ratings\u2014 published 1850",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1404810944l/12296._SY75_.jpg"
        },
        {
            "title": "The Republic (Paperback)",
            "author": "Plato",
            "desc": "avg rating 3.96 \u2014 210,968 ratings\u2014 published -400",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1386925655l/30289._SY75_.jpg"
        },
        {
            "title": "The 48 Laws of Power (Paperback)",
            "author": "Robert Greene",
            "desc": "avg rating 4.12 \u2014 185,098 ratings\u2014 published 1998",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1694722764l/1303._SX50_.jpg"
        },
        {
            "title": "Frankenstein: The 1818 Text (Paperback)",
            "author": "Mary Wollstonecraft Shelley",
            "desc": "avg rating 3.88 \u2014 1,676,642 ratings\u2014 published 1818",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1631088473l/35031085._SY75_.jpg"
        },
        {
            "title": "The Last Tree: A seed of hope (Hardcover)",
            "author": "Luke Adam Hawker",
            "desc": "avg rating 4.44 \u2014 653 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1670272133l/63099282._SX50_.jpg"
        },
        {
            "title": "Beyond Good and Evil (Paperback)",
            "author": "Friedrich Nietzsche",
            "desc": "avg rating 4.03 \u2014 101,192 ratings\u2014 published 1886",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388607391l/12321._SY75_.jpg"
        },
        {
            "title": "A Gentleman in Moscow (Paperback)",
            "author": "Amor Towles",
            "desc": "avg rating 4.33 \u2014 591,286 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1718915012l/34066798._SY75_.jpg"
        },
        {
            "title": "The Princess Bride (Paperback)",
            "author": "William Goldman",
            "desc": "avg rating 4.27 \u2014 916,336 ratings\u2014 published 1973",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327903636l/21787._SY75_.jpg"
        },
        {
            "title": "Solito (Hardcover)",
            "author": "Javier Zamora",
            "desc": "avg rating 4.48 \u2014 52,925 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1643985393l/59900688._SY75_.jpg"
        },
        {
            "title": "We Deserve Monuments (Hardcover)",
            "author": "Jas Hammonds",
            "desc": "avg rating 4.29 \u2014 9,322 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1644414847l/58484187._SX50_.jpg"
        },
        {
            "title": "All the Bright Places (Hardcover)",
            "author": "Jennifer Niven",
            "desc": "avg rating 4.12 \u2014 589,720 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1404331702l/18460392._SY75_.jpg"
        },
        {
            "title": "Their Eyes Were Watching God (Paperback)",
            "author": "Zora Neale Hurston",
            "desc": "avg rating 3.98 \u2014 360,097 ratings\u2014 published 1937",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1368072803l/37415._SY75_.jpg"
        },
        {
            "title": "Rogues: True Stories of Grifters, Killers, Rebels and Crooks (Hardcover)",
            "author": "Patrick Radden Keefe",
            "desc": "avg rating 4.01 \u2014 17,180 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1636978568l/59148726._SY75_.jpg"
        },
        {
            "title": "We Were Never Here (Hardcover)",
            "author": "Andrea Bartz",
            "desc": "avg rating 3.50 \u2014 133,282 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1627923495l/56084054._SY75_.jpg"
        },
        {
            "title": "Factory Girls (Paperback)",
            "author": "Michelle Gallen",
            "desc": "avg rating 3.72 \u2014 4,002 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1648427692l/59892267._SX50_.jpg"
        },
        {
            "title": "The Final Empire (Mistborn, #1)",
            "author": "Brandon Sanderson",
            "desc": "avg rating 4.48 \u2014 771,911 ratings\u2014 published 2006",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1617768316l/68428._SY75_.jpg"
        },
        {
            "title": "The Bars Are Ours: Histories and Cultures of Gay Bars in America,1960 and After (Hardcover)",
            "author": "Lucas Hilderbrand",
            "desc": "avg rating 4.19 \u2014 42 ratings\u2014 published",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1682202627l/123840843._SX50_.jpg"
        },
        {
            "title": "Tomb of Sand (Paperback)",
            "author": "Geetanjali Shree",
            "desc": "avg rating 3.69 \u2014 3,387 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1628126156l/58703758._SY75_.jpg"
        },
        {
            "title": "Salt Houses (Hardcover)",
            "author": "Hala Alyan",
            "desc": "avg rating 4.00 \u2014 17,568 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1474820735l/30971664._SY75_.jpg"
        },
        {
            "title": "Before We Were Strangers (Paperback)",
            "author": "Renee Carlino",
            "desc": "avg rating 4.07 \u2014 132,178 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1438012963l/23309634._SY75_.jpg"
        },
        {
            "title": "The Driver's Seat (Paperback)",
            "author": "Muriel Spark",
            "desc": "avg rating 3.61 \u2014 10,750 ratings\u2014 published 1970",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348828782l/668282._SY75_.jpg"
        },
        {
            "title": "Wild Thorns (Paperback)",
            "author": "Sahar Khalifeh",
            "desc": "avg rating 3.83 \u2014 1,188 ratings\u2014 published 1976",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1701193085l/218442._SY75_.jpg"
        },
        {
            "title": "After Dark (Hardcover)",
            "author": "Haruki Murakami",
            "desc": "avg rating 3.74 \u2014 172,515 ratings\u2014 published 2004",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1437952316l/17803._SY75_.jpg"
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        }
    ],
    "Capricorne": [
        {
            "title": "A Court of Mist and Fury (A Court of Thorns and Roses, #2)",
            "author": "Sarah J. Maas",
            "desc": "avg rating 4.65 \u2014 2,426,448 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1620325671l/50659468._SY75_.jpg"
        },
        {
            "title": "The Song of Achilles (Paperback)",
            "author": "Madeline Miller",
            "desc": "avg rating 4.32 \u2014 1,658,144 ratings\u2014 published 2011",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1357177533l/13623848._SY75_.jpg"
        },
        {
            "title": "The Seven Husbands of Evelyn Hugo (Hardcover)",
            "author": "Taylor Jenkins Reid",
            "desc": "avg rating 4.41 \u2014 3,401,879 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1664458703l/32620332._SY75_.jpg"
        },
        {
            "title": "Pride and Prejudice (Paperback)",
            "author": "Jane Austen",
            "desc": "avg rating 4.29 \u2014 4,409,300 ratings\u2014 published 1813",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1320399351l/1885._SY75_.jpg"
        },
        {
            "title": "Six of Crows (Six of Crows, #1)",
            "author": "Leigh Bardugo",
            "desc": "avg rating 4.48 \u2014 1,021,958 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1651710803l/23437156._SY75_.jpg"
        },
        {
            "title": "Fourth Wing (The Empyrean, #1)",
            "author": "Rebecca Yarros",
            "desc": "avg rating 4.57 \u2014 2,169,931 ratings\u2014 published 2023",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1701980900l/61431922._SY75_.jpg"
        },
        {
            "title": "The Book Thief (Kindle Edition)",
            "author": "Markus Zusak",
            "desc": "avg rating 4.39 \u2014 2,669,714 ratings\u2014 published 2005",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1522157426l/19063._SY75_.jpg"
        },
        {
            "title": "1984 (Paperback)",
            "author": "George Orwell",
            "desc": "avg rating 4.19 \u2014 4,859,128 ratings\u2014 published 1949",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1657781256l/61439040._SX50_.jpg"
        },
        {
            "title": "The Hunger Games (The Hunger Games, #1)",
            "author": "Suzanne Collins",
            "desc": "avg rating 4.34 \u2014 9,037,696 ratings\u2014 published 2008",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1586722975l/2767052._SX50_.jpg"
        },
        {
            "title": "A Little Life (Hardcover)",
            "author": "Hanya Yanagihara",
            "desc": "avg rating 4.32 \u2014 737,768 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1446469353l/22822858._SY75_.jpg"
        },
        {
            "title": "The Secret History (Paperback)",
            "author": "Donna Tartt",
            "desc": "avg rating 4.17 \u2014 838,194 ratings\u2014 published 1992",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1451554846l/29044._SY75_.jpg"
        },
        {
            "title": "Kingdom of Ash (Throne of Glass, #7)",
            "author": "Sarah J. Maas",
            "desc": "avg rating 4.70 \u2014 735,034 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1673567331l/76715522._SY75_.jpg"
        },
        {
            "title": "Crooked Kingdom (Six of Crows, #2)",
            "author": "Leigh Bardugo",
            "desc": "avg rating 4.59 \u2014 687,173 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1456172607l/22299763._SY75_.jpg"
        },
        {
            "title": "Harry Potter and the Sorcerer\u2019s Stone (Harry Potter, #1)",
            "author": "J.K. Rowling",
            "desc": "avg rating 4.47 \u2014 10,501,077 ratings\u2014 published 1997",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1598823299l/42844155._SX50_.jpg"
        },
        {
            "title": "Dune (Dune, #1)",
            "author": "Frank Herbert",
            "desc": "avg rating 4.28 \u2014 1,468,391 ratings\u2014 published 1965",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1555447414l/44767458._SY75_.jpg"
        },
        {
            "title": "To Kill a Mockingbird (Paperback)",
            "author": "Harper Lee",
            "desc": "avg rating 4.26 \u2014 6,379,637 ratings\u2014 published 1960",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1553383690l/2657._SY75_.jpg"
        },
        {
            "title": "All the Light We Cannot See (Hardcover)",
            "author": "Anthony Doerr",
            "desc": "avg rating 4.31 \u2014 1,777,404 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1451445646l/18143977._SY75_.jpg"
        },
        {
            "title": "A \u200bCourt of Silver Flames (A Court of Thorns and Roses, #4)",
            "author": "Sarah J. Maas",
            "desc": "avg rating 4.47 \u2014 1,496,887 ratings\u2014 published 2021",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1602570691l/53138095._SY75_.jpg"
        },
        {
            "title": "Harry Potter and the Prisoner of Azkaban (Harry Potter, #3)",
            "author": "J.K. Rowling",
            "desc": "avg rating 4.58 \u2014 4,405,089 ratings\u2014 published 1999",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1630547330l/5._SY75_.jpg"
        },
        {
            "title": "Throne of Glass (Throne of Glass, #1)",
            "author": "Sarah J. Maas",
            "desc": "avg rating 4.18 \u2014 1,815,843 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1673566495l/76703559._SY75_.jpg"
        },
        {
            "title": "Jane Eyre (Paperback)",
            "author": "Charlotte Bront\u00eb",
            "desc": "avg rating 4.15 \u2014 2,163,208 ratings\u2014 published 1847",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1557343311l/10210._SY75_.jpg"
        },
        {
            "title": "A Court of Wings and Ruin (A Court of Thorns and Roses, #3)",
            "author": "Sarah J. Maas",
            "desc": "avg rating 4.47 \u2014 2,024,586 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1585623092l/50659472._SX50_.jpg"
        },
        {
            "title": "The Perks of Being a Wallflower (Paperback)",
            "author": "Stephen Chbosky",
            "desc": "avg rating 4.23 \u2014 1,866,010 ratings\u2014 published 1999",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1650033115l/22628._SX50_.jpg"
        },
        {
            "title": "Where the Crawdads Sing (ebook)",
            "author": "Delia Owens",
            "desc": "avg rating 4.38 \u2014 3,222,771 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1582135294l/36809135._SY75_.jpg"
        },
        {
            "title": "Red, White & Royal Blue (Paperback)",
            "author": "Casey McQuiston",
            "desc": "avg rating 4.07 \u2014 1,086,184 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1566742512l/41150487._SY75_.jpg"
        },
        {
            "title": "The Handmaid\u2019s Tale (The Handmaid's Tale, #1)",
            "author": "Margaret Atwood",
            "desc": "avg rating 4.14 \u2014 2,148,239 ratings\u2014 published 1985",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1578028274l/38447._SY75_.jpg"
        },
        {
            "title": "A Game of Thrones (A Song of Ice and Fire, #1)",
            "author": "George R.R. Martin",
            "desc": "avg rating 4.44 \u2014 2,575,430 ratings\u2014 published 1996",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1562726234l/13496._SY75_.jpg"
        },
        {
            "title": "The Picture of Dorian Gray (Paperback)",
            "author": "Oscar Wilde",
            "desc": "avg rating 4.13 \u2014 1,638,875 ratings\u2014 published 1890",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1546103428l/5297._SY75_.jpg"
        },
        {
            "title": "Daisy Jones & The Six (Hardcover)",
            "author": "Taylor Jenkins Reid",
            "desc": "avg rating 4.20 \u2014 1,631,019 ratings\u2014 published 2019",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1580255154l/40597810._SY75_.jpg"
        },
        {
            "title": "Circe (Hardcover)",
            "author": "Madeline Miller",
            "desc": "avg rating 4.23 \u2014 1,158,720 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1565909496l/35959740._SY75_.jpg"
        },
        {
            "title": "Harry Potter and the Goblet of Fire (Harry Potter, #4)",
            "author": "J.K. Rowling",
            "desc": "avg rating 4.57 \u2014 3,864,706 ratings\u2014 published 2000",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1554006152l/6._SX50_.jpg"
        },
        {
            "title": "Harry Potter and the Deathly Hallows (Harry Potter, #7)",
            "author": "J.K. Rowling",
            "desc": "avg rating 4.62 \u2014 3,847,009 ratings\u2014 published 2007",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1663805647l/136251._SY75_.jpg"
        },
        {
            "title": "A Thousand Splendid Suns (Hardcover)",
            "author": "Khaled Hosseini",
            "desc": "avg rating 4.44 \u2014 1,597,930 ratings\u2014 published 2007",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1655336738l/128029._SY75_.jpg"
        },
        {
            "title": "The Night Circus (Hardcover)",
            "author": "Erin Morgenstern",
            "desc": "avg rating 4.01 \u2014 1,020,792 ratings\u2014 published 2011",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1387124618l/9361589._SY75_.jpg"
        },
        {
            "title": "Normal People (Hardcover)",
            "author": "Sally Rooney",
            "desc": "avg rating 3.81 \u2014 1,550,993 ratings\u2014 published 2018",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1571423190l/41057294._SY75_.jpg"
        },
        {
            "title": "Queen of Shadows (Throne of Glass, #4)",
            "author": "Sarah J. Maas",
            "desc": "avg rating 4.61 \u2014 1,003,892 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1673566810l/76707900._SY75_.jpg"
        },
        {
            "title": "Pachinko (Kindle Edition)",
            "author": "Min Jin Lee",
            "desc": "avg rating 4.34 \u2014 520,137 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1529845599l/34051011._SY75_.jpg"
        },
        {
            "title": "The Little Prince (Paperback)",
            "author": "Antoine de Saint-Exup\u00e9ry",
            "desc": "avg rating 4.33 \u2014 2,211,220 ratings\u2014 published 1943",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1367545443l/157993._SY75_.jpg"
        },
        {
            "title": "The Alchemist (Paperback)",
            "author": "Paulo Coelho",
            "desc": "avg rating 3.91 \u2014 3,221,408 ratings\u2014 published 1993",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1654371463l/18144590._SY75_.jpg"
        },
        {
            "title": "Lolita (Paperback)",
            "author": "Vladimir Nabokov",
            "desc": "avg rating 3.88 \u2014 880,899 ratings\u2014 published 1955",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1377756377l/7604._SY75_.jpg"
        },
        {
            "title": "It Ends with Us (It Ends with Us, #1)",
            "author": "Colleen Hoover",
            "desc": "avg rating 4.13 \u2014 3,948,021 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1688011813l/27362503._SY75_.jpg"
        },
        {
            "title": "The Lightning Thief (Percy Jackson and the Olympians, #1)",
            "author": "Rick Riordan",
            "desc": "avg rating 4.31 \u2014 3,171,750 ratings\u2014 published 2005",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1400602609l/28187._SY75_.jpg"
        },
        {
            "title": "Crimen y castigo (Paperback)",
            "author": "Fyodor Dostoevsky",
            "desc": "avg rating 4.27 \u2014 953,342 ratings\u2014 published 1866",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1171499594l/103582._SY75_.jpg"
        },
        {
            "title": "The Giver (The Giver, #1)",
            "author": "Lois Lowry",
            "desc": "avg rating 4.12 \u2014 2,589,228 ratings\u2014 published 1993",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1342493368l/3636._SY75_.jpg"
        },
        {
            "title": "A Court of Thorns and Roses (A Court of Thorns and Roses, #1)",
            "author": "Sarah J. Maas",
            "desc": "avg rating 4.18 \u2014 3,188,464 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1620324329l/50659467._SY75_.jpg"
        },
        {
            "title": "Catching Fire (The Hunger Games, #2)",
            "author": "Suzanne Collins",
            "desc": "avg rating 4.33 \u2014 3,742,918 ratings\u2014 published 2009",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1586722941l/6148028._SY75_.jpg"
        },
        {
            "title": "The Great Gatsby (Paperback)",
            "author": "F. Scott Fitzgerald",
            "desc": "avg rating 3.93 \u2014 5,443,126 ratings\u2014 published 1925",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1490528560l/4671._SY75_.jpg"
        },
        {
            "title": "The Final Empire (Mistborn, #1)",
            "author": "Brandon Sanderson",
            "desc": "avg rating 4.48 \u2014 771,911 ratings\u2014 published 2006",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1617768316l/68428._SY75_.jpg"
        },
        {
            "title": "Slaughterhouse-Five (Paperback)",
            "author": "Kurt Vonnegut Jr.",
            "desc": "avg rating 4.10 \u2014 1,402,827 ratings\u2014 published 1969",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1440319389l/4981._SY75_.jpg"
        },
        {
            "title": "Book Lovers (Hardcover)",
            "author": "Emily Henry",
            "desc": "avg rating 4.12 \u2014 1,251,420 ratings\u2014 published 2022",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1638867089l/58690308._SY75_.jpg"
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        }
    ],
    "bac": [
        {
            "title": "Harry Potter and the Sorcerer\u2019s Stone (Harry Potter, #1)",
            "author": "J.K. Rowling",
            "desc": "avg rating 4.47 \u2014 10,501,174 ratings\u2014 published 1997",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1598823299l/42844155._SX50_.jpg"
        },
        {
            "title": "1984 (Paperback)",
            "author": "George Orwell",
            "desc": "avg rating 4.19 \u2014 4,859,183 ratings\u2014 published 1949",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1657781256l/61439040._SX50_.jpg"
        },
        {
            "title": "To Kill a Mockingbird (Paperback)",
            "author": "Harper Lee",
            "desc": "avg rating 4.26 \u2014 6,379,669 ratings\u2014 published 1960",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1553383690l/2657._SY75_.jpg"
        },
        {
            "title": "The Hunger Games (The Hunger Games, #1)",
            "author": "Suzanne Collins",
            "desc": "avg rating 4.34 \u2014 9,037,781 ratings\u2014 published 2008",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1586722975l/2767052._SX50_.jpg"
        },
        {
            "title": "Harry Potter and the Prisoner of Azkaban (Harry Potter, #3)",
            "author": "J.K. Rowling",
            "desc": "avg rating 4.58 \u2014 4,405,139 ratings\u2014 published 1999",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1630547330l/5._SY75_.jpg"
        },
        {
            "title": "Harry Potter and the Deathly Hallows (Harry Potter, #7)",
            "author": "J.K. Rowling",
            "desc": "avg rating 4.62 \u2014 3,847,038 ratings\u2014 published 2007",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1663805647l/136251._SY75_.jpg"
        },
        {
            "title": "Pride and Prejudice (Paperback)",
            "author": "Jane Austen",
            "desc": "avg rating 4.29 \u2014 4,409,324 ratings\u2014 published 1813",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1320399351l/1885._SY75_.jpg"
        },
        {
            "title": "The Book Thief (Kindle Edition)",
            "author": "Markus Zusak",
            "desc": "avg rating 4.39 \u2014 2,669,725 ratings\u2014 published 2005",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1522157426l/19063._SY75_.jpg"
        },
        {
            "title": "Harry Potter and the Half-Blood Prince (Harry Potter, #6)",
            "author": "J.K. Rowling",
            "desc": "avg rating 4.58 \u2014 3,406,445 ratings\u2014 published 2005",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1587697303l/1._SX50_.jpg"
        },
        {
            "title": "The Song of Achilles (Paperback)",
            "author": "Madeline Miller",
            "desc": "avg rating 4.32 \u2014 1,658,175 ratings\u2014 published 2011",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1357177533l/13623848._SY75_.jpg"
        },
        {
            "title": "Harry Potter and the Order of the Phoenix (Harry Potter, #5)",
            "author": "J.K. Rowling",
            "desc": "avg rating 4.50 \u2014 3,520,003 ratings\u2014 published 2003",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1546910265l/2._SY75_.jpg"
        },
        {
            "title": "Harry Potter and the Goblet of Fire (Harry Potter, #4)",
            "author": "J.K. Rowling",
            "desc": "avg rating 4.57 \u2014 3,864,732 ratings\u2014 published 2000",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1554006152l/6._SX50_.jpg"
        },
        {
            "title": "The Name of the Wind (The Kingkiller Chronicle, #1)",
            "author": "Patrick Rothfuss",
            "desc": "avg rating 4.52 \u2014 1,003,865 ratings\u2014 published 2007",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1704917687l/186074._SY75_.jpg"
        },
        {
            "title": "Six of Crows (Six of Crows, #1)",
            "author": "Leigh Bardugo",
            "desc": "avg rating 4.48 \u2014 1,021,968 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1651710803l/23437156._SY75_.jpg"
        },
        {
            "title": "The Little Prince (Paperback)",
            "author": "Antoine de Saint-Exup\u00e9ry",
            "desc": "avg rating 4.33 \u2014 2,211,250 ratings\u2014 published 1943",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1367545443l/157993._SY75_.jpg"
        },
        {
            "title": "Harry Potter and the Chamber of Secrets (Harry Potter, #2)",
            "author": "J.K. Rowling",
            "desc": "avg rating 4.43 \u2014 4,118,837 ratings\u2014 published 1998",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1474169725l/15881._SY75_.jpg"
        },
        {
            "title": "The Seven Husbands of Evelyn Hugo (Hardcover)",
            "author": "Taylor Jenkins Reid",
            "desc": "avg rating 4.41 \u2014 3,401,941 ratings\u2014 published 2017",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1664458703l/32620332._SY75_.jpg"
        },
        {
            "title": "The Catcher in the Rye (Paperback)",
            "author": "J.D. Salinger",
            "desc": "avg rating 3.80 \u2014 3,644,418 ratings\u2014 published 1951",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1398034300l/5107._SY75_.jpg"
        },
        {
            "title": "The Fault in Our Stars (Hardcover)",
            "author": "John Green",
            "desc": "avg rating 4.13 \u2014 5,340,018 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1660273739l/11870085._SX50_.jpg"
        },
        {
            "title": "The Kite Runner (Paperback)",
            "author": "Khaled Hosseini",
            "desc": "avg rating 4.35 \u2014 3,257,236 ratings\u2014 published 2003",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1579036753l/77203._SY75_.jpg"
        },
        {
            "title": "The Secret History (Paperback)",
            "author": "Donna Tartt",
            "desc": "avg rating 4.17 \u2014 838,215 ratings\u2014 published 1992",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1451554846l/29044._SY75_.jpg"
        },
        {
            "title": "One Hundred Years of Solitude (Mass Market Paperback)",
            "author": "Gabriel Garc\u00eda M\u00e1rquez",
            "desc": "avg rating 4.12 \u2014 1,009,548 ratings\u2014 published 1967",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327881361l/320._SX50_.jpg"
        },
        {
            "title": "Ender\u2019s Game (Ender's Saga, #1)",
            "author": "Orson Scott Card",
            "desc": "avg rating 4.31 \u2014 1,409,714 ratings\u2014 published 1985",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1408303130l/375802._SY75_.jpg"
        },
        {
            "title": "A Game of Thrones (A Song of Ice and Fire, #1)",
            "author": "George R.R. Martin",
            "desc": "avg rating 4.44 \u2014 2,575,446 ratings\u2014 published 1996",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1562726234l/13496._SY75_.jpg"
        },
        {
            "title": "Crimen y castigo (Paperback)",
            "author": "Fyodor Dostoevsky",
            "desc": "avg rating 4.27 \u2014 953,346 ratings\u2014 published 1866",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1171499594l/103582._SY75_.jpg"
        },
        {
            "title": "The Alchemist (Paperback)",
            "author": "Paulo Coelho",
            "desc": "avg rating 3.91 \u2014 3,221,419 ratings\u2014 published 1993",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1654371463l/18144590._SY75_.jpg"
        },
        {
            "title": "Catching Fire (The Hunger Games, #2)",
            "author": "Suzanne Collins",
            "desc": "avg rating 4.33 \u2014 3,742,948 ratings\u2014 published 2009",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1586722941l/6148028._SY75_.jpg"
        },
        {
            "title": "The Perks of Being a Wallflower (Paperback)",
            "author": "Stephen Chbosky",
            "desc": "avg rating 4.23 \u2014 1,866,018 ratings\u2014 published 1999",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1650033115l/22628._SX50_.jpg"
        },
        {
            "title": "The Great Gatsby (Paperback)",
            "author": "F. Scott Fitzgerald",
            "desc": "avg rating 3.93 \u2014 5,443,146 ratings\u2014 published 1925",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1490528560l/4671._SY75_.jpg"
        },
        {
            "title": "A Little Life (Hardcover)",
            "author": "Hanya Yanagihara",
            "desc": "avg rating 4.32 \u2014 737,782 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1446469353l/22822858._SY75_.jpg"
        },
        {
            "title": "The Picture of Dorian Gray (Paperback)",
            "author": "Oscar Wilde",
            "desc": "avg rating 4.13 \u2014 1,638,886 ratings\u2014 published 1890",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1546103428l/5297._SY75_.jpg"
        },
        {
            "title": "A Court of Mist and Fury (A Court of Thorns and Roses, #2)",
            "author": "Sarah J. Maas",
            "desc": "avg rating 4.65 \u2014 2,426,534 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1620325671l/50659468._SY75_.jpg"
        },
        {
            "title": "It Ends with Us (It Ends with Us, #1)",
            "author": "Colleen Hoover",
            "desc": "avg rating 4.13 \u2014 3,948,089 ratings\u2014 published 2016",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1688011813l/27362503._SY75_.jpg"
        },
        {
            "title": "The Hobbit (The Lord of the Rings, #0)",
            "author": "J.R.R. Tolkien",
            "desc": "avg rating 4.29 \u2014 4,167,689 ratings\u2014 published 1937",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1546071216l/5907._SY75_.jpg"
        },
        {
            "title": "Animal Farm (Mass Market Paperback)",
            "author": "George Orwell",
            "desc": "avg rating 3.99 \u2014 4,075,456 ratings\u2014 published 1945",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1325861570l/170448._SY75_.jpg"
        },
        {
            "title": "The Lightning Thief (Percy Jackson and the Olympians, #1)",
            "author": "Rick Riordan",
            "desc": "avg rating 4.31 \u2014 3,171,760 ratings\u2014 published 2005",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1400602609l/28187._SY75_.jpg"
        },
        {
            "title": "Jane Eyre (Paperback)",
            "author": "Charlotte Bront\u00eb",
            "desc": "avg rating 4.15 \u2014 2,163,218 ratings\u2014 published 1847",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1557343311l/10210._SY75_.jpg"
        },
        {
            "title": "A Thousand Splendid Suns (Hardcover)",
            "author": "Khaled Hosseini",
            "desc": "avg rating 4.44 \u2014 1,597,941 ratings\u2014 published 2007",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1655336738l/128029._SY75_.jpg"
        },
        {
            "title": "Divergent (Divergent, #1)",
            "author": "Veronica Roth",
            "desc": "avg rating 4.14 \u2014 4,119,125 ratings\u2014 published 2011",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1618526890l/13335037._SY75_.jpg"
        },
        {
            "title": "All the Light We Cannot See (Hardcover)",
            "author": "Anthony Doerr",
            "desc": "avg rating 4.31 \u2014 1,777,420 ratings\u2014 published 2014",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1451445646l/18143977._SY75_.jpg"
        },
        {
            "title": "The Hitchhiker\u2019s Guide to the Galaxy (Hitchhiker's Guide to the Galaxy, #1)",
            "author": "Douglas Adams",
            "desc": "avg rating 4.23 \u2014 1,901,099 ratings\u2014 published 1979",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1531891848l/11._SY75_.jpg"
        },
        {
            "title": "The Girl with the Dragon Tattoo (Millennium, #1)",
            "author": "Stieg Larsson",
            "desc": "avg rating 4.17 \u2014 3,272,204 ratings\u2014 published 2005",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1684638853l/2429135._SX50_.jpg"
        },
        {
            "title": "Dune (Dune, #1)",
            "author": "Frank Herbert",
            "desc": "avg rating 4.28 \u2014 1,468,407 ratings\u2014 published 1965",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1555447414l/44767458._SY75_.jpg"
        },
        {
            "title": "The Final Empire (Mistborn, #1)",
            "author": "Brandon Sanderson",
            "desc": "avg rating 4.48 \u2014 771,930 ratings\u2014 published 2006",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1617768316l/68428._SY75_.jpg"
        },
        {
            "title": "The Fellowship of the Ring (The Lord of the Rings, #1)",
            "author": "J.R.R. Tolkien",
            "desc": "avg rating 4.40 \u2014 2,890,143 ratings\u2014 published 1954",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1654215925l/61215351._SY75_.jpg"
        },
        {
            "title": "A Court of Thorns and Roses (A Court of Thorns and Roses, #1)",
            "author": "Sarah J. Maas",
            "desc": "avg rating 4.18 \u2014 3,188,559 ratings\u2014 published 2015",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1620324329l/50659467._SY75_.jpg"
        },
        {
            "title": "The Way of Kings (The Stormlight Archive, #1)",
            "author": "Brandon Sanderson",
            "desc": "avg rating 4.66 \u2014 548,167 ratings\u2014 published 2010",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1659905828l/7235533._SY75_.jpg"
        },
        {
            "title": "The Wise Man\u2019s Fear (The Kingkiller Chronicle, #2)",
            "author": "Patrick Rothfuss",
            "desc": "avg rating 4.55 \u2014 579,424 ratings\u2014 published 2011",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1452624392l/1215032._SY75_.jpg"
        },
        {
            "title": "The Master and Margarita (Paperback)",
            "author": "Mikhail Bulgakov",
            "desc": "avg rating 4.29 \u2014 374,997 ratings\u2014 published 1967",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327867963l/117833._SY75_.jpg"
        },
        {
            "title": "East of Eden (Paperback)",
            "author": "John Steinbeck",
            "desc": "avg rating 4.42 \u2014 564,944 ratings\u2014 published 1952",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1639969375l/4406._SY75_.jpg"
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        }
    ],
    "dumb": [
        {
            "title": "Charlotte\u2019s Web (Paperback)",
            "author": "E.B. White",
            "desc": "avg rating 4.20 \u2014 1,908,728 ratings\u2014 published 1952",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1628267712l/24178._SY75_.jpg"
        },
        {
            "title": "Where the Wild Things Are (Paperback)",
            "author": "Maurice Sendak",
            "desc": "avg rating 4.25 \u2014 1,022,522 ratings\u2014 published 1963",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1384434560l/19543._SX50_.jpg"
        },
        {
            "title": "Harry Potter and the Sorcerer\u2019s Stone (Harry Potter, #1)",
            "author": "J.K. Rowling",
            "desc": "avg rating 4.47 \u2014 10,501,174 ratings\u2014 published 1997",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1598823299l/42844155._SX50_.jpg"
        },
        {
            "title": "The Giving Tree (Hardcover)",
            "author": "Shel Silverstein",
            "desc": "avg rating 4.38 \u2014 1,164,085 ratings\u2014 published 1964",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1725807591l/370493._SX50_.jpg"
        },
        {
            "title": "Green Eggs and Ham (Hardcover)",
            "author": "Dr. Seuss",
            "desc": "avg rating 4.31 \u2014 799,288 ratings\u2014 published 1960",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1673212751l/23772._SX50_.jpg"
        },
        {
            "title": "Matilda (Paperback)",
            "author": "Roald Dahl",
            "desc": "avg rating 4.33 \u2014 1,004,275 ratings\u2014 published 1988",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388793265l/39988._SY75_.jpg"
        },
        {
            "title": "Charlie and the Chocolate Factory (Charlie Bucket, #1)",
            "author": "Roald Dahl",
            "desc": "avg rating 4.16 \u2014 875,770 ratings\u2014 published 1964",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1309211401l/6310._SY75_.jpg"
        },
        {
            "title": "The Lion, the Witch and the Wardrobe (Chronicles of Narnia, #1)",
            "author": "C.S. Lewis",
            "desc": "avg rating 4.24 \u2014 2,901,631 ratings\u2014 published 1950",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1353029077l/100915._SY75_.jpg"
        },
        {
            "title": "Where the Sidewalk Ends (Hardcover)",
            "author": "Shel Silverstein",
            "desc": "avg rating 4.34 \u2014 1,433,546 ratings\u2014 published 1974",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1168052448l/30119._SX50_.jpg"
        },
        {
            "title": "The Very Hungry Caterpillar (Board book)",
            "author": "Eric Carle",
            "desc": "avg rating 4.33 \u2014 522,692 ratings\u2014 published 1969",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1603739265l/4948._SX50_.jpg"
        },
        {
            "title": "The Cat in the Hat (The Cat in the Hat, #1)",
            "author": "Dr. Seuss",
            "desc": "avg rating 4.19 \u2014 555,927 ratings\u2014 published 1957",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1468890477l/233093._SX50_.jpg"
        },
        {
            "title": "Harry Potter and the Chamber of Secrets (Harry Potter, #2)",
            "author": "J.K. Rowling",
            "desc": "avg rating 4.43 \u2014 4,118,837 ratings\u2014 published 1998",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1474169725l/15881._SY75_.jpg"
        },
        {
            "title": "Harry Potter and the Prisoner of Azkaban (Harry Potter, #3)",
            "author": "J.K. Rowling",
            "desc": "avg rating 4.58 \u2014 4,405,139 ratings\u2014 published 1999",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1630547330l/5._SY75_.jpg"
        },
        {
            "title": "A Wrinkle in Time (Time Quintet, #1)",
            "author": "Madeleine L'Engle",
            "desc": "avg rating 3.98 \u2014 1,229,862 ratings\u2014 published 1962",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1507963312l/33574273._SX50_.jpg"
        },
        {
            "title": "The Little Prince (Paperback)",
            "author": "Antoine de Saint-Exup\u00e9ry",
            "desc": "avg rating 4.33 \u2014 2,211,250 ratings\u2014 published 1943",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1367545443l/157993._SY75_.jpg"
        },
        {
            "title": "James and the Giant Peach (Hardcover)",
            "author": "Roald Dahl",
            "desc": "avg rating 4.03 \u2014 488,012 ratings\u2014 published 1961",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1320412586l/6689._SX50_.jpg"
        },
        {
            "title": "Goodnight Moon (Hardcover)",
            "author": "Margaret Wise Brown",
            "desc": "avg rating 4.31 \u2014 381,267 ratings\u2014 published 1947",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1439223893l/32929._SX50_.jpg"
        },
        {
            "title": "The BFG (Paperback)",
            "author": "Roald Dahl",
            "desc": "avg rating 4.23 \u2014 497,587 ratings\u2014 published 1982",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327872673l/6319._SY75_.jpg"
        },
        {
            "title": "Harry Potter and the Goblet of Fire (Harry Potter, #4)",
            "author": "J.K. Rowling",
            "desc": "avg rating 4.57 \u2014 3,864,732 ratings\u2014 published 2000",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1554006152l/6._SX50_.jpg"
        },
        {
            "title": "The Secret Garden (Hardcover)",
            "author": "Frances Hodgson Burnett",
            "desc": "avg rating 4.16 \u2014 1,214,711 ratings\u2014 published 1911",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327873635l/2998._SY75_.jpg"
        },
        {
            "title": "The Lightning Thief (Percy Jackson and the Olympians, #1)",
            "author": "Rick Riordan",
            "desc": "avg rating 4.31 \u2014 3,171,760 ratings\u2014 published 2005",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1400602609l/28187._SY75_.jpg"
        },
        {
            "title": "Oh, the Places You\u2019ll Go! (Hardcover)",
            "author": "Dr. Seuss",
            "desc": "avg rating 4.37 \u2014 418,883 ratings\u2014 published 1990",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1630510695l/191139._SX50_.jpg"
        },
        {
            "title": "Harry Potter and the Order of the Phoenix (Harry Potter, #5)",
            "author": "J.K. Rowling",
            "desc": "avg rating 4.50 \u2014 3,520,003 ratings\u2014 published 2003",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1546910265l/2._SY75_.jpg"
        },
        {
            "title": "Harry Potter and the Half-Blood Prince (Harry Potter, #6)",
            "author": "J.K. Rowling",
            "desc": "avg rating 4.58 \u2014 3,406,445 ratings\u2014 published 2005",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1587697303l/1._SX50_.jpg"
        },
        {
            "title": "Harry Potter and the Deathly Hallows (Harry Potter, #7)",
            "author": "J.K. Rowling",
            "desc": "avg rating 4.62 \u2014 3,847,038 ratings\u2014 published 2007",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1663805647l/136251._SY75_.jpg"
        },
        {
            "title": "Winnie-the-Pooh (Winnie-the-Pooh, #1)",
            "author": "A.A. Milne",
            "desc": "avg rating 4.38 \u2014 470,184 ratings\u2014 published 1926",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1298440130l/99107._SY75_.jpg"
        },
        {
            "title": "Holes (Holes, #1)",
            "author": "Louis Sachar",
            "desc": "avg rating 4.00 \u2014 1,255,966 ratings\u2014 published 1998",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1618269830l/38709._SX50_.jpg"
        },
        {
            "title": "How the Grinch Stole Christmas! (Hardcover)",
            "author": "Dr. Seuss",
            "desc": "avg rating 4.38 \u2014 424,313 ratings\u2014 published 1957",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327958149l/113946._SX50_.jpg"
        },
        {
            "title": "The Lorax (Hardcover)",
            "author": "Dr. Seuss",
            "desc": "avg rating 4.35 \u2014 352,104 ratings\u2014 published 1971",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1705520064l/7784._SX50_.jpg"
        },
        {
            "title": "The Phantom Tollbooth (Paperback)",
            "author": "Norton Juster",
            "desc": "avg rating 4.20 \u2014 294,007 ratings\u2014 published 1961",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1558858485l/378._SX50_.jpg"
        },
        {
            "title": "The Witches (Paperback)",
            "author": "Roald Dahl",
            "desc": "avg rating 4.18 \u2014 407,594 ratings\u2014 published 1981",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1351707720l/6327._SY75_.jpg"
        },
        {
            "title": "Wonder (Wonder, #1)",
            "author": "R.J. Palacio",
            "desc": "avg rating 4.37 \u2014 1,125,055 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1545695751l/11387515._SY75_.jpg"
        },
        {
            "title": "The Bad Beginning (A Series of Unfortunate Events, #1)",
            "author": "Lemony Snicket",
            "desc": "avg rating 4.01 \u2014 539,337 ratings\u2014 published 1999",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1436737029l/78411._SX50_.jpg"
        },
        {
            "title": "Pippi Longstocking (Pippi L\u00e5ngstrump, #1)",
            "author": "Astrid Lindgren",
            "desc": "avg rating 4.15 \u2014 203,235 ratings\u2014 published 1945",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1519300455l/19302._SX50_.jpg"
        },
        {
            "title": "The Wonderful Wizard of Oz (Oz, #1)",
            "author": "L. Frank Baum",
            "desc": "avg rating 4.00 \u2014 469,711 ratings\u2014 published 1900",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1398003737l/236093._SY75_.jpg"
        },
        {
            "title": "Anne of Green Gables (Anne of Green Gables, #1)",
            "author": "L.M. Montgomery",
            "desc": "avg rating 4.32 \u2014 1,023,882 ratings\u2014 published 1908",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1615094578l/8127._SY75_.jpg"
        },
        {
            "title": "If You Give a Mouse a Cookie (If You Give...)",
            "author": "Laura Joffe Numeroff",
            "desc": "avg rating 4.29 \u2014 302,687 ratings\u2014 published 1985",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1276046901l/767680._SX50_.jpg"
        },
        {
            "title": "Bridge to Terabithia (Kindle Edition)",
            "author": "Katherine Paterson",
            "desc": "avg rating 4.05 \u2014 561,521 ratings\u2014 published 1977",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1532478367l/40940121._SY75_.jpg"
        },
        {
            "title": "One Fish, Two Fish, Red Fish, Blue Fish (Hardcover)",
            "author": "Dr. Seuss",
            "desc": "avg rating 4.18 \u2014 207,980 ratings\u2014 published 1960",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1165640023l/7770._SX50_.jpg"
        },
        {
            "title": "From the Mixed-Up Files of Mrs. Basil E. Frankweiler (Paperback)",
            "author": "E.L. Konigsburg",
            "desc": "avg rating 4.16 \u2014 214,055 ratings\u2014 published 1967",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327784751l/3980._SY75_.jpg"
        },
        {
            "title": "The Giver (The Giver, #1)",
            "author": "Lois Lowry",
            "desc": "avg rating 4.12 \u2014 2,589,236 ratings\u2014 published 1993",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1342493368l/3636._SY75_.jpg"
        },
        {
            "title": "The Velveteen Rabbit (Paperback)",
            "author": "Margery Williams Bianco",
            "desc": "avg rating 4.31 \u2014 263,099 ratings\u2014 published 1922",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1347748913l/144974._SX50_.jpg"
        },
        {
            "title": "Little House in the Big Woods (Little House, #1)",
            "author": "Laura Ingalls Wilder",
            "desc": "avg rating 4.21 \u2014 275,169 ratings\u2014 published 1932",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1621570121l/8337._SX50_.jpg"
        },
        {
            "title": "Love You Forever (Paperback)",
            "author": "Robert Munsch",
            "desc": "avg rating 4.37 \u2014 241,056 ratings\u2014 published 1986",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348832754l/310259._SX50_.jpg"
        },
        {
            "title": "The One and Only Ivan (The One and Only #1)",
            "author": "Katherine Applegate",
            "desc": "avg rating 4.27 \u2014 195,493 ratings\u2014 published 2012",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1424981397l/11594337._SX50_.jpg"
        },
        {
            "title": "A Light in the Attic (Hardcover)",
            "author": "Shel Silverstein",
            "desc": "avg rating 4.36 \u2014 457,954 ratings\u2014 published 1981",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1427169918l/30118._SX50_.jpg"
        },
        {
            "title": "Corduroy (Hardcover)",
            "author": "Don Freeman",
            "desc": "avg rating 4.33 \u2014 224,192 ratings\u2014 published 1968",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1347517273l/231850._SX50_.jpg"
        },
        {
            "title": "The Tale of Peter Rabbit (World of Beatrix Potter, #1)",
            "author": "Beatrix Potter",
            "desc": "avg rating 4.22 \u2014 250,888 ratings\u2014 published 1902",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1485118382l/19321._SX50_.jpg"
        },
        {
            "title": "Are You My Mother? (Paperback)",
            "author": "P.D. Eastman",
            "desc": "avg rating 4.21 \u2014 246,893 ratings\u2014 published 1960",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1389098758l/197084._SX50_.jpg"
        },
        {
            "title": "Brown Bear, Brown Bear, What Do You See? (Board book)",
            "author": "Bill Martin Jr.",
            "desc": "avg rating 4.26 \u2014 185,032 ratings\u2014 published 1967",
            "img": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1430155496l/759611._SY75_.jpg"
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        },
        {
            "title": "",
            "author": "",
            "desc": "",
            "img": ""
        }
    ]
}



open("books.txt","w").write(json.dumps(books))
def get_horoscope(dob):
    """
    Get the horoscope sign based on the date of birth.

    Args:
        dob (str): Date of birth in the format 'YYYY-MM-DD'.

    Returns:
        str: The horoscope sign in French.
    """
    # Extract month and day from the date
    from datetime import datetime
    
    try:
        date = datetime.strptime(dob, "%Y-%m-%d")
        day = date.day
        month = date.month
    except ValueError:
        return "Format de date invalide. Utilisez 'YYYY-MM-DD'."

    # Horoscope ranges with French names
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Verseau"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Poissons"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Bélier"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taureau"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gémeaux"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Lion"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Vierge"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Balance"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpion"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittaire"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorne"

    return "Signe inconnu"

def get_horoscopeDesc(dob):

    # Extract month and day from the date
    from datetime import datetime
    
    try:
        date = datetime.strptime(dob, "%Y-%m-%d")
        day = date.day
        month = date.month
    except ValueError:
        return "Format de date invalide. Utilisez 'YYYY-MM-DD'."

    # Horoscope ranges with French names
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return """Tu es quelqu’un d’assez unique, tu sais ? On sent tout de suite que tu tiens à ta liberté, que c’est quelque chose de non négociable pour toi. Ce qui est admirable, c’est ta capacité à te débrouiller tout seul, sans jamais trop dépendre des autres. Et puis, quand il faut décider, tu le fais sans hésitation, avec une assurance qui force le respect.

Ce que j’aime chez toi, c’est ton énergie créative. Tu as toujours mille idées en tête, une sorte d’effervescence constante, et tu n’as pas peur de casser les codes ou de chambouler les habitudes. Ça fait de toi une personne passionnante à côtoyer, imprévisible dans le bon sens du terme.

Et puis, ton esprit, il est brillant. Tu as ce mélange rare d’intelligence et de sociabilité. Tu t’adaptes à tout et à tout le monde, mais sans jamais perdre ton authenticité. Tu es sincèrement tourné vers les autres, et ton enthousiasme pour les projets collectifs est contagieux.

Mais c’est vrai, parfois, tu peux être têtu. Quand tu es persuadé d’avoir raison, c’est presque mission impossible de te faire changer d’avis. Et ce côté un peu détaché, qui donne l’impression que tu te fiches de tout, peut être déroutant. Pourtant, je sais bien que ce n’est qu’une façade.

Ce que les gens doivent comprendre, c’est que tu ne supportes pas la routine ni qu’on essaie de t’enfermer dans des règles. Tu as besoin de bouger, de tester, d’expérimenter, quitte à parfois partir dans des directions inattendues. Et oui, ton humour un peu provocateur peut surprendre, mais ça fait partie de ton charme. Avec toi, rien n’est jamais ennuyeux, et c’est ça qui te rend si spécial."""
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return """Tu es quelqu’un de profondément connecté aux autres, presque comme si tu ressentais les choses à un niveau que peu peuvent atteindre. Ta sensibilité est un véritable cadeau, même si parfois, ça peut te rendre un peu vulnérable. Mais c’est aussi ce qui fait de toi une personne tellement unique : tu comprends les gens, souvent mieux qu’ils ne se comprennent eux-mêmes.

J’adore la façon dont ton imagination semble sans limites. Tu as ce talent incroyable pour voir la beauté là où personne ne regarde, pour rêver grand et t’évader dans des univers qui n’appartiennent qu’à toi. Avec toi, on a l’impression que tout est possible.

Tu as un cœur immense, prêt à aider, à écouter, à soutenir. Mais parfois, j’ai l’impression que tu donnes tellement aux autres que tu t’oublies un peu. Fais attention à toi aussi, parce que ta douceur et ta générosité méritent d’être protégées.

Ce que j’admire le plus, c’est ton intuition. C’est comme si tu savais toujours quoi faire, quoi dire, ou même quoi ressentir avant tout le monde. Avec toi, il n’y a pas besoin de longs discours, tu captes les choses au vol, et ça, c’est une vraie force.

Tu es un rêveur, oui, mais un rêveur qui apporte une touche de magie dans tout ce qu’il fait. Et ça, c’est précieux, tu sais ?"""
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return """Avec toi, il y a toujours une énergie incroyable. Tu fonces, tu n’hésites pas, et ça inspire les autres à suivre. J’adore ton courage, ta façon d’affronter les choses de face, sans chercher à te cacher ou à tergiverser. Quand tu veux quelque chose, tu vas le chercher, et franchement, c’est impressionnant.

Tu as ce feu en toi, cette détermination qui fait que rien ne semble impossible. Peu importe les obstacles, tu trouves toujours un moyen de les contourner ou de les détruire. Ce que j’aime aussi, c’est que tu sais entraîner les autres avec toi, avec une telle passion qu’on a envie de te suivre, peu importe où tu vas.

Bien sûr, parfois, tu peux être un peu têtu. Mais en même temps, ça fait partie de ton charme : tu sais ce que tu veux, et tu n’abandonnes jamais. Cette force de caractère, c’est ce qui te rend si unique.

Tu as aussi un côté direct qui peut surprendre, mais au moins, avec toi, pas de faux-semblants. Tu dis ce que tu penses, et ça, c’est rare et précieux. Avec toi, les choses bougent, évoluent, et on ne s’ennuie jamais. Tu es une vraie bouffée d’énergie, et c’est toujours un plaisir de te voir en action."""
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return """Avec toi, il y a une stabilité rassurante. Tu es quelqu’un sur qui on peut vraiment compter, peu importe les circonstances. Ta patience et ta force tranquille mettent tout le monde à l’aise, et franchement, c’est un vrai cadeau d’avoir quelqu’un comme toi dans sa vie.

Ce que j’admire, c’est ta capacité à aller au bout des choses. Quand tu décides de t’investir dans quelque chose, tu ne fais pas les choses à moitié. Tu es déterminé, fiable, et tu sais construire des bases solides, que ce soit dans tes projets ou dans tes relations.

J’aime aussi ton côté terre-à-terre. Tu sais apprécier les plaisirs simples, que ce soit un bon repas, un moment de calme, ou quelque chose de beau que tu as pris le temps de créer. Tu as ce lien spécial avec ce qui est réel et concret, et ça inspire les autres à ralentir et à profiter de l’instant présent.

Bien sûr, parfois, tu peux être un peu têtu. Quand tu as une idée en tête, difficile de te faire changer d’avis. Mais c’est aussi ce qui fait ta force : tu sais ce que tu veux, et tu tiens bon. Avec toi, les choses avancent dans la bonne direction, et c’est toujours solide. Tu as cette capacité rare à équilibrer force et douceur, et c’est ce qui te rend vraiment unique."""
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return """Avec toi, il y a toujours une conversation qui démarre, une idée qui fuse, un éclat de rire qui éclaire la pièce. Tu as ce don incroyable de rendre chaque moment plus vivant, plus intéressant. Ton esprit est rapide, curieux, et tu sembles toujours savoir quelque chose de fascinant ou avoir une anecdote à raconter.

Ce que j’aime chez toi, c’est que tu t’adaptes à tout le monde. Peu importe la situation ou la personne en face de toi, tu trouves toujours un terrain d’entente, un sujet qui connecte. Tu as une énergie sociale contagieuse, et on ne peut qu’admirer ta capacité à créer des liens presque instantanément.

Je te trouve aussi super malin. Tu as cette façon unique de jongler avec les idées, de voir les choses sous des angles auxquels personne ne pense. Et puis, il y a ton côté imprévisible : on ne sait jamais où la prochaine conversation va nous mener avec toi, et franchement, c’est ce qui rend tout ça tellement excitant.

C’est vrai, parfois, on peut avoir du mal à te suivre parce que tu as mille projets et idées en tête, mais c’est ce qui fait ton charme. Tu es toujours en mouvement, toujours en train de découvrir, d’apprendre, de créer. Avec toi, il n’y a jamais de place pour la monotonie, et c’est ce qui te rend si unique."""
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return """Avec toi, on se sent tout de suite chez soi. Tu as cette façon unique de créer un cocon autour des gens que tu aimes, une sorte de refuge où ils peuvent se sentir protégés et compris. Ton instinct est incroyable, comme si tu pouvais ressentir ce dont les autres ont besoin avant même qu’ils ne le disent.

Tu es profondément attaché aux choses qui comptent vraiment : les liens, les souvenirs, les moments partagés. Avec toi, tout prend une dimension plus douce, plus intime. Tu donnes tellement aux autres, parfois au point de te mettre un peu en retrait, mais c’est ta façon de montrer à quel point tu tiens à eux.

Ce que j’admire chez toi, c’est ta force discrète. On pourrait penser que ta sensibilité te rend fragile, mais c’est tout le contraire. Tu as cette capacité à tenir bon, à garder le cap, même quand les choses deviennent difficiles. Et ce qui est beau, c’est que tu fais tout ça en restant toi-même, sans jamais perdre cette authenticité qui te rend si spécial.

Tu as un cœur énorme, et ça se voit dans tout ce que tu fais. Avec toi, on se sent écouté, compris et aimé d’une manière qui ne demande rien en retour. Et honnêtement, c’est un vrai cadeau d’avoir quelqu’un comme toi autour de soi."""
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return """Avec toi, il y a toujours cette aura incroyable, comme si tout gravite autour de ta présence. Tu as une confiance naturelle qui attire les gens, et on sent que tu es né pour briller. Ce que j’aime, c’est que tu ne fais pas ça pour écraser les autres, mais plutôt pour les inspirer. Tu as une générosité qui illumine tout autour de toi.

Tu as ce talent pour rassembler, pour créer un espace où chacun se sent valorisé, et ça, c’est une vraie force. Quand tu t’investis, tu le fais avec tout ton cœur, que ce soit pour un projet, une amitié ou une idée. Et cette passion, elle est contagieuse.

C’est vrai, parfois tu peux avoir besoin qu’on reconnaisse tout ce que tu fais, et honnêtement, tu le mérites. Tu travailles dur, et tu donnes tellement de toi-même que c’est normal d’attendre un peu de gratitude en retour. Mais ce qui est beau chez toi, c’est que tu es toujours prêt à partager ta lumière avec les autres.

Tu es une personne qui porte fièrement ses valeurs, et on peut toujours compter sur toi pour défendre ce qui te tient à cœur. Avec toi, on se sent soutenu, encouragé, et en sécurité. Tu es une vraie force de la nature, et ta présence fait toute la différence."""
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return """Avec toi, on sent tout de suite que les détails comptent. Tu as cette capacité incroyable à tout analyser, à tout comprendre, et surtout à tout organiser avec une précision impressionnante. Rien ne t’échappe, et c’est vraiment rassurant de savoir que tu es là pour garder les choses sous contrôle.

Ce que j’admire, c’est ta fiabilité. Quand tu dis que tu vas faire quelque chose, on peut être sûr que ce sera fait, et bien fait. Tu as un sens du devoir et une rigueur qui forcent le respect. Mais ce qui te rend encore plus spécial, c’est que derrière cette apparence sérieuse, tu es profondément attentif aux autres. Tu remarques ce dont ils ont besoin, parfois même avant qu’ils ne le sachent eux-mêmes.

Parfois, tu peux être un peu dur avec toi-même, toujours à vouloir que tout soit parfait. Mais tu sais quoi ? Tu n’as pas besoin de l’être. Ce que tu fais et qui tu es, c’est déjà tellement précieux. Ton envie de bien faire, de te dépasser, c’est une de tes plus grandes forces, mais rappelle-toi de souffler un peu parfois.

Avec toi, on se sent en sécurité, compris, et même inspiré à faire mieux. Tu es une personne qui élève les autres, tout en restant humble et authentique. Et ça, c’est rare et précieux."""
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return """Avec toi, tout semble plus harmonieux. Tu as ce talent naturel pour apaiser les tensions, trouver le juste équilibre et faire en sorte que tout le monde se sente bien. Tu réfléchis toujours avant d’agir, pesant le pour et le contre, cherchant la solution la plus juste. C’est tellement agréable d’avoir quelqu’un comme toi, qui cherche toujours à créer une atmosphère de paix.

Ce que j’admire, c’est ta manière de voir la beauté dans les choses. Tu as un vrai sens de l’esthétique, une capacité à rendre tout plus élégant, que ce soit dans ce que tu fais, dis, ou même dans la façon dont tu te comportes. Et puis, tu es tellement sociable, toujours là pour écouter, pour comprendre, pour créer des liens.

Mais ce que j’aime encore plus, c’est ton côté profondément loyal. Quand tu tiens à quelqu’un, tu es là pour de vrai, prêt à faire des efforts pour que les choses fonctionnent. Parfois, tu peux hésiter un peu, c’est vrai, mais c’est parce que tu veux faire ce qu’il y a de mieux pour tout le monde. Et ça, c’est une vraie qualité.

Avec toi, on se sent compris, apprécié, et entouré d’une belle énergie. Tu as cette capacité rare à rassembler les gens, à construire des ponts entre eux. C’est un vrai cadeau que tu apportes aux autres."""
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return """Avec toi, il y a toujours cette intensité incroyable, comme si tout ce que tu faisais ou ressentais avait une profondeur qu’on ne trouve pas chez tout le monde. Tu as une présence qui ne passe jamais inaperçue, et franchement, on sent que tu es quelqu’un de vrai, sans masque ni superficialité.

Ce que j’admire chez toi, c’est ta capacité à aller jusqu’au bout des choses. Quand tu veux quelque chose, rien ni personne ne peut t’arrêter. Tu as une détermination et une force intérieure qui forcent le respect. Mais ce qui est encore plus impressionnant, c’est ton intuition. C’est comme si tu savais toujours ce qui se passe, comme si rien ne pouvait t’échapper.

Tu as un côté mystérieux aussi, et c’est fascinant. On n’arrive jamais à te cerner complètement, et c’est ce qui te rend si intriguant. Mais quand on a la chance de te connaître, on découvre quelqu’un de loyal, passionné et profondément protecteur envers ceux que tu aimes.

C’est vrai que parfois, tu peux être un peu exigeant ou direct, mais ça montre simplement que tu ne fais pas dans la demi-mesure. Et puis, avec toi, on sait où on va : il n’y a pas de faux-semblants. Tu es intense, mais c’est ce qui te rend si unique et inoubliable."""
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return """Avec toi, on sent tout de suite cette envie d’explorer, de découvrir tout ce que le monde a à offrir. Tu as une énergie contagieuse, une soif de liberté et d’aventure qui inspire tout le monde autour de toi. On dirait que tu es toujours en quête de quelque chose de plus grand, de plus profond, et c’est tellement fascinant.

Ce que j’aime chez toi, c’est ton optimisme. Même quand les choses ne vont pas comme prévu, tu trouves toujours une raison de sourire, une solution, ou une leçon à tirer. Tu as cette capacité à voir le verre à moitié plein, et franchement, c’est rafraîchissant. 

Tu es quelqu’un qui pense grand, qui rêve loin, et qui n’a pas peur de viser haut. Et puis, ton honnêteté… c’est parfois brut de décoffrage, mais au moins, on sait toujours où on en est avec toi. Tu dis ce que tu penses, sans détour, et ça fait de toi une personne authentique, sur qui on peut vraiment compter.

Mais ce qui te rend vraiment unique, c’est ton côté chaleureux et généreux. Tu as ce don pour rassembler les gens, pour partager des idées, des histoires, ou même simplement des moments de joie. Avec toi, on se sent vivant, comme si tout était possible. Franchement, c’est un vrai bonheur de t’avoir dans les parages."""
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return """Tu as une force intérieure qui force le respect. On sent tout de suite que tu es quelqu’un de fiable, quelqu’un sur qui on peut compter, peu importe les circonstances. Ton sérieux et ta détermination, c’est impressionnant, vraiment. Quand tu te fixes un objectif, rien ne peut t’arrêter, et tu as cette patience rare qui te permet de construire quelque chose de solide et durable.

J’admire aussi ta façon de réfléchir avant d’agir. Tu ne fais rien au hasard, tout est calculé, mais pas dans le mauvais sens : c’est juste que tu veux que les choses soient bien faites. Ça fait de toi une personne incroyablement rassurante, parce qu’on sait que, avec toi, tout est sous contrôle.

Mais ce que j’aime encore plus, c’est que derrière cette façade parfois un peu réservée, il y a une chaleur et une sensibilité que tu ne montres pas toujours facilement. Tu prends soin des tiens d’une manière qui est discrète, mais tellement sincère. 

Ce qui est incroyable, c’est que tu arrives à garder les pieds sur terre tout en ayant de grandes ambitions. Tu montres à tout le monde que réussir, ça demande du travail, mais que ça en vaut toujours la peine. Avec toi, on se sent motivé à donner le meilleur de soi-même. Franchement, tu es un exemple."""

    return ""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prenom = request.form.get("prenom")
        nom = request.form.get("nom")
        dob = request.form.get("dob")
        religion = request.form.get("religion")
        studyLevel = request.form.get("studyLevel")
        
        if(studyLevel == "noDegree"):
            sl = "Inconscience et ignorance de base , Parfois, j’ai l’impression que vous avancez dans la vie sans vraiment vous arrêter pour réfléchir à ce qui vous entoure ou à vos choix. C’est comme si les choses allaient simplement d’elles-mêmes, sans que vous les questionniez. Cela arrive à tout le monde, mais je crois sincèrement que si vous preniez un peu de recul, vous pourriez découvrir des aspects intéressants qui vous échappent pour l’instant."
        elif(studyLevel == "bac"):
            sl = "Prise de conscience limitée , Je vois que vous commencez à remarquer certaines choses, à vous poser des questions sur ce qui vous entoure. C’est un signe que vous cherchez à mieux comprendre, et c’est vraiment une belle étape. Cependant, vous avez encore tendance à vous arrêter à la surface, sans toujours aller au fond des choses. Je pense que si vous osiez explorer plus profondément, vous pourriez vraiment découvrir des perspectives qui vous enrichiraient."
        elif(studyLevel == "bac+2"):
            sl = "Éveil intellectuel et réflexion critique , Ce que j’apprécie chez vous, c’est que vous prenez désormais le temps de réfléchir par vous-même. Vous n’acceptez plus aveuglément ce qu’on vous dit, et vous cherchez des réponses qui résonnent vraiment avec vos convictions. C’est une preuve d’une grande maturité intellectuelle. Vous avez cette capacité à poser des questions pertinentes et à voir au-delà des évidences, et cela montre à quel point vous progressez dans votre réflexion."    
        elif (studyLevel == "bac+5"):
            sl ="Pleine conscience et intelligence maîtrisée , À ce stade, je dois dire que vous êtes vraiment impressionnant(e). Vous avez une compréhension claire des choses, une capacité rare à analyser les situations avec profondeur et à prendre des décisions éclairées. Ce qui est encore plus admirable, c’est que vous utilisez votre conscience et votre intelligence non seulement pour vous, mais aussi pour aider et inspirer ceux qui vous entourent. Votre présence et votre esprit apportent quelque chose de précieux à votre environnement."
        if(religion == "islam"):
            rg = "Vous avez cette force intérieure qui vient de votre foi. Ce que je ressens chez vous, c’est une dévotion sincère et un profond respect pour les valeurs et principes qui vous guident. Vous trouvez dans vos prières, vos actions et votre mode de vie une discipline et une paix qui semblent vous ancrer solidement. C’est inspirant de voir à quel point votre spiritualité influence positivement votre manière d’être et votre relation avec les autres."
        elif (religion == "jeff"):
            rg ="Ce que je perçois chez vous, c’est une connexion très spéciale avec votre histoire, vos traditions et vos valeurs. Vous incarnez un bel équilibre entre le respect des enseignements anciens et leur application dans le monde moderne. Votre foi semble être un guide pour vous, non seulement dans vos choix personnels, mais aussi dans la manière dont vous interagissez avec ceux qui vous entourent. Cette relation profonde avec votre héritage montre une grande force et une fidélité à ce qui compte vraiment pour vous."
        elif(religion == "christians"):
            rg = "Vous avez une lumière en vous qui semble nourrie par votre foi. Ce que j’admire, c’est la manière dont vous cherchez à vivre en accord avec vos croyances, en mettant souvent l’amour, le pardon et la générosité au centre de vos actions. Vous inspirez par votre capacité à voir le bien chez les autres et à porter vos valeurs avec simplicité et sincérité. C’est beau de voir une foi qui se traduit par des actes concrets dans votre quotidien."
        elif(religion == "sans"):
            rg = "Ce que je vois chez vous, c’est une liberté de pensée qui vous permet de chercher vos propres réponses et de tracer votre chemin sans suivre un cadre religieux précis. Vous semblez trouver votre sens dans vos expériences, vos relations et vos réflexions personnelles. Ce qui est admirable, c’est votre ouverture à d’autres points de vue et votre manière de rester fidèle à vos convictions, sans forcément avoir besoin de vous rattacher à des doctrines. Cela montre une grande force d’esprit et une autonomie remarquable."
        suggested_books = []
        if(studyLevel != "noDegree"):
            suggested_books = suggested_books + random.choices(books.get("bac", []) ,k=20)
        suggested_books = suggested_books + random.choices(books.get(religion, []) ,k=10)
        if(studyLevel == "noDegree"):
                suggested_books = suggested_books + random.choices(books.get("dumb", []) ,k=10)
        suggested_books = suggested_books + random.choices(books.get(get_horoscope(dob), []) ,k=10)
        for book in suggested_books:
            if (book.get("name") == ""):
                suggested_books.remove(book)
        print(suggested_books)
        horo = str(f"""
        <p>Chère/cher {nom} {prenom},</p>
        <p>Vous êtes une personne {sl}. Vous avez cette particularité de {rg}.</p>
        <p>Vous portez en vous une richesse unique qui se traduit par {get_horoscopeDesc(dob)}.</p>
        <p>Continuez à explorer et à enrichir ce chemin, car vous avez en vous les qualités pour inspirer et grandir encore davantage.</p>
        """).replace("..",".")
        return render_template(
            "index.html",
            suggestion=True,
            prenom=prenom,
            nom=nom,
            dob=dob,
            religion=religion,
            studyLevel=studyLevel,
            books = suggested_books,
            horo=horo , 
        )

    return render_template("index.html", suggestion=False)

if __name__ == "__main__":
    app.run(debug=True)
