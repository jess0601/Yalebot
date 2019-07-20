from .base import Module
from yalelaundry import YaleLaundry
import os


class Laundry(Module):
    DESCRIPTION = "Get information about Yale's laundry rooms"
    api = YaleLaundry(os.environ.get("YALE_API_KEY"))

    def response(self, query, message):
        if query:
            room = self.api.room(query)
            avail = room.availability
            total = room.totals
            items = [(room.name, f"({room.campus_name})")]
            items += [("Washers available", f"{avail.washer}/{total.washer}"),
                      ("Dryers available", f"{avail.dryer}/{total.dryer}")]
            for appliance in room.appliances:
                items.append((appliance.type + " " + appliance.label, appliance.status_raw))
            return self.bullet_list(items, embellish_first=True)
        else:
            rooms = self.api.rooms()
            items = []
            for room in rooms:
                avail = room.availability
                total = room.totals
                items.append((room.name,
                              f"{avail.washer}/{total.washer} washers, {avail.dryer}/{total.dryer} dryers currently available"))
            return self.bullet_list(items)
