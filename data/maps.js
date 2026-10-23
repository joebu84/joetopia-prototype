// OPTIONAL HAND-MADE MAPS. Any engine node without an entry here gets a generated map
// from its biome (see data/world.js). A map is 20 columns x 15 rows.
// Legend: '#' wall (blocks)  '.' floor  ',' floor variant  'D' decor (blocks)  '~' water (blocks)
// exits: door cells for the place's exits, used in order (the exit back to the parent node
//        uses 'back'). Each entry [x, y, side] where side is N/S/W/E (which way you walk out).
// slots: cells for people, shops and things to do, used in order.
window.JOETOPIA_MAPS = {
  village: {
    rows: [
      '####################',
      '####################',
      '#,......,....,.....#',
      '#..D..........D....#',
      '#..................#',
      '#,.....,,,,,,......#',
      '#......,~~~~,......#',
      '#..D...,~~~~,...D..#',
      '#......,,,,,,......#',
      '#..................#',
      '#....,........,....#',
      '#..D...........D...#',
      '#..................#',
      '#..................#',
      '####################',
    ],
    exits: [[4, 1, 'N'], [9, 1, 'N'], [14, 1, 'N'], [19, 7, 'E'], [0, 7, 'W'], [19, 11, 'E'], [0, 11, 'W']],
    back: [9, 14, 'S'],
    slots: [[5, 9], [13, 9], [9, 4], [5, 4], [14, 4], [6, 12], [13, 12]],
  },
};
