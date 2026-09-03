.. figure:: _static/banner.png

Geoinformatics Research Days 2027
======================

The *Geoinformatics Research Days* (GRD) event is the annual gathering for geoinformatics experts, 
which has been organized by the member universities of the Finnish University Network for Geoinformatics 
(`Fiuginet <https://www.geoportti.fi/services/skills-development/fiuginet/>`_) 
for over 10 years. The event will take place on **May 10-12, 2027**, and will be organized by University of Helsinki together 
with the Fiuginet network, hosted in Helsinki, Finland.

.. The program includes the **Final Event of the Geospatial Challenge Camp (GCC)**, where multidisciplinary 
.. teams of early-career researchers and students present solutions to real-world sustainability challenges using geospatial data and technologies. 
.. Learn more at the `Geospatial Challenge Camp website <https://challenge-camp.geoportti.fi/>`_.

Important Dates
=================

- Abstract Submission Opens: November, 2026, exact date TBA
- Abstract Submission Deadline: February, 2027, exact date TBA
- Notification of Acceptance: TBA
- Registration Opens: TBA
- Presenter Registration Deadline: TBA
- Registration Closes: TBA
- Conference Dates: May 10-12, 2027

Call for Abstracts
======================

TBA

.. Geoinformatics Research Days welcomes contributions from all areas of geospatial research and applications, providing an open platform 
.. for sharing ideas, methods, and innovations across the discipline. This year's **spotlight theme, Geospatial Intelligence for Sustainable 
.. Futures**, explores how emerging forms of spatial intelligence and AI are transforming our understanding of people, places, and the 
.. complex systems that connect them. We invite submissions that link AI-driven geospatial innovation with questions of sustainability, 
.. resilience, biodiversity, accessibility, and spatial justice across scales—from everyday mobility to global change.

Topics of Interest
-------------------

TBA

Submission Guidelines
----------------------

Presenters are invited to submit an abstract of a maximum of 300 words in English.

All submitted abstracts will be peer-reviewed to ensure the quality of the contributions. 
All accepted submissions will be given a chance to present their work at the *Geoinformatics Research Days 2027*.

Abstract Submission
--------------------
.. attention::

    Coming soon
    
    .. button-link:: 
            :color: primary
            :shadow:
            :align: center

            👉 TBA


Scientific Committee
====================

TBA

Program
========

TBA

Keynotes
----------

TBA



Venue
======

The event will be held at **Main Building, City Center Campus, University of Helsinki**, Helsinki, Finland. 

More details TBA

.. raw:: html

  <div>
  <hr>

  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

  <style>
    .grd-pin {
      width: 28px; height: 28px;
      border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      box-shadow: 0 1px 4px rgba(0,0,0,0.4);
      border: 2px solid white;
    }
    .grd-pin svg { width: 15px; height: 15px; fill: white; }
    .grd-popup-row { display: flex; align-items: center; gap: 10px; margin-bottom: 6px; }

    #grd-venue-map { height: 450px; width: 100%; max-width: 700px; border: 1px solid #ccc; }
    @media (max-width: 480px) {
      #grd-venue-map { height: 320px; }
    }
  </style>

  <div id="grd-venue-map"></div>

  <script>
    var map = L.map('grd-venue-map', {
      dragging: !L.Browser.mobile,
      tap: !L.Browser.mobile
    }).setView([60.169490, 24.949412], 16);

    map.touchZoom.enable();

    var osmLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      maxZoom: 19
    }).addTo(map);

    var satelliteLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
      attribution: 'Tiles &copy; Esri — Source: Esri, Maxar, Earthstar Geographics',
      maxZoom: 19
    });

    L.control.layers(
      { "OSM": osmLayer, "Satellite": satelliteLayer },
      null,
      { collapsed: true }
    ).addTo(map);

    // Venue pin (building icon)
    var buildingSVG = '<svg viewBox="0 0 448 512"><path d="M436.5 32H11.5C5.1 32 0 37.1 0 43.5v13c0 6.4 5.1 11.5 11.5 11.5H32v384c0 8.8 7.2 16 16 16h96V368c0-8.8 7.2-16 16-16h96c8.8 0 16 7.2 16 16v112h96c8.8 0 16-7.2 16-16V68h20.5c6.4 0 11.5-5.1 11.5-11.5v-13C448 37.1 442.9 32 436.5 32zM160 240c0 8.8-7.2 16-16 16h-32c-8.8 0-16-7.2-16-16v-32c0-8.8 7.2-16 16-16h32c8.8 0 16 7.2 16 16v32zm0-96c0 8.8-7.2 16-16 16h-32c-8.8 0-16-7.2-16-16v-32c0-8.8 7.2-16 16-16h32c8.8 0 16 7.2 16 16v32zm96 96c0 8.8-7.2 16-16 16h-32c-8.8 0-16-7.2-16-16v-32c0-8.8 7.2-16 16-16h32c8.8 0 16 7.2 16 16v32zm0-96c0 8.8-7.2 16-16 16h-32c-8.8 0-16-7.2-16-16v-32c0-8.8 7.2-16 16-16h32c8.8 0 16 7.2 16 16v32zm96 96c0 8.8-7.2 16-16 16h-32c-8.8 0-16-7.2-16-16v-32c0-8.8 7.2-16 16-16h32c8.8 0 16 7.2 16 16v32zm0-96c0 8.8-7.2 16-16 16h-32c-8.8 0-16-7.2-16-16v-32c0-8.8 7.2-16 16-16h32c8.8 0 16 7.2 16 16v32z"/></svg>';

    var venueIcon = L.divIcon({
      className: '',
      html: '<div class="grd-pin" style="background:#d63e2a;">' + buildingSVG + '</div>',
      iconSize: [28, 28],
      iconAnchor: [14, 14],
      popupAnchor: [0, -14]
    });

    var copySVG = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#555" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>';

    var venuePopup = `
      <div style="min-width: 220px; padding: 4px 2px;">
        <b>University of Helsinki – Main Building</b>
        <div class="grd-popup-row" style="margin-top: 8px;">
          <span id="grd-address">Fabianinkatu 33, 00100 Helsinki</span>
          <span onclick="
               navigator.clipboard.writeText(document.getElementById('grd-address').innerText);
               document.getElementById('grd-copy-feedback').style.display = 'inline';
               setTimeout(function(){ document.getElementById('grd-copy-feedback').style.display = 'none'; }, 1500);
             "
             title="Copy address"
             style="cursor: pointer; display: flex; align-items: center; padding: 8px; margin: -8px;">${copySVG}</span>
          <span id="grd-copy-feedback" style="display:none; color: green; font-size: 0.85em;">Copied</span>
        </div>
        <div style="margin-top: 4px;">
          <a href="https://www.google.com/maps/dir/?api=1&destination=60.169490,24.949412" target="_blank">Get directions (Google Maps)</a>
        </div>
      </div>
    `;

    L.marker([60.169490, 24.949412], {icon: venueIcon})
      .addTo(map)
      .bindPopup(venuePopup)
      .openPopup();
  </script>

  <hr>
  </div>

Registration
==============

.. Places are limited, so we encourage you to register early to secure your spot.

We warmly invite all interested in the field to participate, including researchers, industry professionals, 
public sector experts, and students.

Details TBA

.. **Registration is open until April 29, 2026.**

.. **Note:** Presenters must register by April 8, 2026.


Practical Information
==============

- **WiFi:** For connection instructions, see the `University WiFi Guide <https://helpdesk.it.helsinki.fi/en/help/11079>`_.
- **Accommodation & travel:** No support is provided. For visitor information and local recommendations, see the `University of Helsinki Visitor Guide <https://www.helsinki.fi/en/about-us/visit-us/guide-visitors>`_.

More details TBA

Contact Us
===============

.. grid:: 1

    .. grid-item-card::

        For questions or further information, please contact us by email at **geoinfo-research-days@helsinki.fi**

Event Partners and Sponsors
===============

.. figure:: _static/sponsors_and_partners.png


.. .. toctree::
..    :maxdepth: 2
..    :caption: Contents:
..    :hidden:

..    Parallel Sessions <pages/parallel_sessions>