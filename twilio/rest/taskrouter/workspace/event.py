# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

from twilio.rest.resources.util import (
    parse_date,
    parse_iso_date,
)
from twilio.rest.resources.base import NextGenInstanceResource
from twilio.rest.resources.base import NextGenListResource


class Event(NextGenInstanceResource):
    """
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: actor_sid
    
        The actor_sid
    
    .. attribute:: actor_type
    
        The actor_type
    
    .. attribute:: actor_url
    
        The actor_url
    
    .. attribute:: description
    
        The description
    
    .. attribute:: event_data
    
        The event_data
    
    .. attribute:: event_date
    
        The event_date
    
    .. attribute:: event_type
    
        The event_type
    
    .. attribute:: resource_sid
    
        The resource_sid
    
    .. attribute:: resource_type
    
        The resource_type
    
    .. attribute:: resource_url
    
        The resource_url
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: source
    
        The source
    
    .. attribute:: source_ip_address
    
        The source_ip_address
    
    .. attribute:: url
    
        The url
    """
    id_key = "sid"

    def load(self, *args, **kwargs):
        super(Event, self).load(*args, **kwargs)
        
        if hasattr(self, "event_date") and self.event_date:
            self.event_date = parse_iso_date(self.event_date)


class Events(NextGenListResource):
    name = "Events"
    mount_name = "events"
    key = "events"
    instance = Event

    def __init__(self, *args, **kwargs):
        super(Events, self).__init__(*args, **kwargs)

    def get(self, sid):
        """
        Get a placeholder for an instance resource.
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Event`
        :returns: A placeholder for a :class:`Event` resource
        """
        return self.get_instance(sid)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`Event`
        
        :param date end_date: The end_date
        :param date start_date: The start_date
        :param str event_type: The event_type
        :param str minutes: The minutes
        :param str reservation_sid: The reservation_sid
        :param str task_queue_sid: The task_queue_sid
        :param str task_sid: The task_sid
        :param str worker_sid: The worker_sid
        :param str workflow_sid: The workflow_sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Event`
        """
        if "end_date" in kwargs:
            kwargs["EndDate"] = parse_date(kwargs["end_date"])
            del kwargs["end_date"]
        if "start_date" in kwargs:
            kwargs["StartDate"] = parse_date(kwargs["start_date"])
            del kwargs["start_date"]
        return self.get_instances(kwargs)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`Event` using an iterator
        
        :param date end_date: The end_date
        :param date start_date: The start_date
        :param str event_type: The event_type
        :param str minutes: The minutes
        :param str reservation_sid: The reservation_sid
        :param str task_queue_sid: The task_queue_sid
        :param str task_sid: The task_sid
        :param str worker_sid: The worker_sid
        :param str workflow_sid: The workflow_sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Event`
        """
        if "end_date" in kwargs:
            kwargs["EndDate"] = parse_date(kwargs["end_date"])
            del kwargs["end_date"]
        if "start_date" in kwargs:
            kwargs["StartDate"] = parse_date(kwargs["start_date"])
            del kwargs["start_date"]
        return super(Events, self).iter(**kwargs)